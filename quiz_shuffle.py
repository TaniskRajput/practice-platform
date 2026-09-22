"""
Deterministic option shuffling for the MCQ banks.

Several banks were transcribed with the correct choice almost always in
position A (Network Security is 88% A, the KN Academy sets are 100% A),
which makes them scoreable without knowing the material. This module
permutes each question's options and remaps the answer index.

The permutation is seeded from (problem id, question number), so the order
is stable across restarts and a browser's saved selections stay meaningful.

Two kinds of questions are handled specially:
  * "All/None of the above" must stay last, so it is pinned there and only
    the remaining options are shuffled.
  * Options that name other options ("Both A and B") break under any
    reordering, so those questions are left exactly as they were.
"""

import random
import re

TERMINAL = re.compile(
    r"^\s*(all|none)\s+of\s+(the\s+)?(above|these)\s*\.?\s*$", re.I
)
# "Both A and B", "Both b and c", "Option C", "Only A" — any option whose
# meaning depends on the position of another option.
LETTER_REF = re.compile(
    r"\b(both|either|only|options?)\s+[a-d]\b|\b[a-d]\s+and\s+[a-d]\b", re.I
)


def _shuffle_question(pid, n, q, slot):
    """Move the answer to `slot` among the movable options and scatter the
    distractors around it. Slots are drawn from a balanced-then-shuffled
    sequence (see shuffle_quiz_options): balanced so the answer key stays
    close to uniform, shuffled so the position is not predictable from the
    question number."""
    options = q["options"]
    if len(options) < 3 or any(LETTER_REF.search(str(o)) for o in options):
        return False

    pinned = [i for i, o in enumerate(options) if TERMINAL.match(str(o))]
    movable = [i for i in range(len(options)) if i not in pinned]
    if q["answer"] in pinned:
        return False  # the answer is "all of the above" — leave it in place

    distractors = [i for i in movable if i != q["answer"]]
    random.Random(f"{pid}:{n}").shuffle(distractors)

    target = slot % len(movable)
    order = distractors[:target] + [q["answer"]] + distractors[target:]
    order += pinned
    if order == list(range(len(options))):
        return False

    q["options"] = [options[i] for i in order]
    q["answer"] = order.index(q["answer"])
    return True


def shuffle_quiz_options(problems):
    """Shuffle every quiz problem's options in place; returns the count.

    The answer's target position comes from a sequence that is balanced
    (equal counts of 0/1/2/3) and then deterministically shuffled. Balanced
    alone is not enough: cycling 0,1,2,3,0,1,2,3 is perfectly uniform and
    perfectly guessable, which is worse than the positional bias it was
    meant to fix."""
    changed = 0
    for p in problems:
        if p.get("judge") != "quiz":
            continue
        n_questions = len(p["questions"])
        slots = [i % 4 for i in range(n_questions)]
        random.Random(f"slots:{p['id']}").shuffle(slots)
        for n, q in enumerate(p["questions"], 1):
            if _shuffle_question(p["id"], n, q, slots[n - 1]):
                changed += 1
    return changed
