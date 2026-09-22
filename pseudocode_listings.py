"""
Pseudocode listings for quiz 29 ("Pseudocode Complete").

The source PDF stores every code block as an image, so the text extraction
that built problems_pseudocode.py produced question stems with no code —
"what is the output of the following pseudocode?" followed by nothing.
These listings were transcribed back from the PDF pages and are spliced
into the question text at load time.

LISTINGS[question_number] -> the code block, as plain text.
"""

LISTINGS = {
    1: """void rearrange(Integer A[], Integer n)
    Integer i = 0, j = n - 1
    while (i < j)
        swap(A[i], A[i+1])
        i = i + 2
        j = j - 1
    end while
    for k = 0 to n-1
        Print A[k]
    end for
end function""",
    2: """void func(String S)
    Integer count = 0
    for i = 0 to length(S) - 1
        if (S[i] == 'A' or S[i] == 'E' or S[i] == 'I' or S[i] == 'O' or S[i] == 'U')
            count = count + 1
        end if
    end for
    Print count
end function""",
    3: """Integer compute(Integer x, Integer y)
    Integer result = (x << 1) ^ y
    return result
end function""",
    4: """void stackOps()
    Stack S = empty
    push(S, 10)
    push(S, 20)
    push(S, 30)
    pop(S)
    push(S, 40)
    Print top(S)
    Print size(S)
end function""",
    5: """void queueOps()
    Queue Q = empty
    enqueue(Q, 5)
    enqueue(Q, 10)
    dequeue(Q)
    enqueue(Q, 15)
    enqueue(Q, 20)
    dequeue(Q)
    Print front(Q)
    Print size(Q)
end function""",
    6: """Integer fib(Integer n)
    if (n <= 1)
        return n
    else
        return fib(n-1) + fib(n-2)
    end if
end function
Print fib(6)""",
    7: """Integer func(Integer A[], Integer i, Integer n)
    if (2*i > n)
        return A[i]
    end if
    Integer sum = 0
    if (2*i <= n)
        sum = sum + func(A, 2*i, n)
    end if
    if (2*i+1 <= n)
        sum = sum + func(A, 2*i+1, n)
    end if
    return sum
end function
Print func(A, 1, 7)""",
    8: """A =
0 1 1 0
1 0 1 1
1 1 0 0
0 1 0 0

Integer funn(Integer A[][], Integer n)
    Integer count = 0
    for i = 0 to n-1
        for j = i+1 to n-1
            if (A[i][j] == 1)
                count = count + 1
            end if
        end for
    end for
    return count
end function
Print funn(A, 4)""",
    9: """void onePass(Integer A[], Integer n)
    for i = 0 to n-2
        if (A[i] > A[i+1])
            swap(A[i], A[i+1])
        end if
    end for
    Print A
end function""",
    10: """Integer funn(Integer A[], Integer n, Integer target)
    Integer low = 0, high = n-1
    while (low <= high)
        Integer mid = (low + high) / 2
        if (A[mid] == target)
            return mid
        else if (A[mid] < target)
            low = mid + 1
        else
            high = mid - 1
        end if
    end while
    return -1
end function
Print funn(A, 7, 10)""",
    11: """Integer a = 5
Integer b = (a++) + (++a)
Print a
Print b""",
    12: """A =
1 2 3
4 5 6
7 8 9

Integer upperSum(Integer A[][], Integer n)
    Integer sum = 0
    for i = 0 to n-1
        for j = 0 to n-1
            if (i < j)
                sum = sum + A[i][j]
            end if
        end for
    end for
    return sum
end function
Print upperSum(A, 3)""",
    13: """void shiftChars(String S)
    for i = 0 to length(S) - 1
        Integer code = ascii(S[i]) + 2
        Print char(code)
    end for
end function""",
    14: """Integer countSetBits(Integer n)
    Integer count = 0
    while (n > 0)
        count = count + (n mod 2)
        n = n / 2
    end while
    return count
end function
Print countSetBits(13)""",
    15: """Character grade(Integer marks)
    if (marks >= 90)
        return 'A'
    else if (marks >= 75)
        return 'B'
    else if (marks >= 50)
        return 'C'
    else
        return 'D'
    end if
end function
Print grade(82)""",
    16: """void funnn(Node head)
    Node prev = NULL
    Node curr = head
    while (curr != NULL)
        Node next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    end while
    printList(prev)
end function""",
    17: """void func(Integer A[], Integer n)
    Map freq = empty
    for i = 0 to n-1
        if (freq.contains(A[i]))
            freq[A[i]] = freq[A[i]] + 1
        else
            freq[A[i]] = 1
        end if
    end for
    Print freq[1]
end function
func(A, 7)""",
    18: """Integer countWays(Integer n)
    Integer dp[n+1]
    dp[0] = 1
    dp[1] = 1
    for i = 2 to n
        dp[i] = dp[i-1] + dp[i-2]
    end for
    return dp[n]
end function
Print countWays(5)""",
    19: """void pattern()
    Integer count = 0
    for i = 1 to 3
        for j = 1 to i
            count = count + j
        end for
    end for
    Print count
end function""",
    20: """Integer funn(String expr)
    Stack S = empty
    for each token in expr (space separated)
        if (token is a number)
            push(S, token)
        else
            Integer b = pop(S)
            Integer a = pop(S)
            if (token == '*')
                push(S, a * b)
            else if (token == '+')
                push(S, a + b)
            end if
        end if
    end for
    return pop(S)
end function
Print funn("5 3 2 * +")""",
    21: """void circularOps()
    CircularQueue Q(capacity=3)
    enqueue(Q, 1)
    enqueue(Q, 2)
    enqueue(Q, 3)
    dequeue(Q)
    enqueue(Q, 4)
    Print front(Q)
    Print rear(Q)
end function""",
    22: """adjList:
0: [1, 2]
1: [0, 3]
2: [0, 3]
3: [1, 2]

void funn(Integer start)
    Queue Q = empty
    Set visited = empty
    enqueue(Q, start)
    visited.add(start)
    while (Q is not empty)
        Integer node = dequeue(Q)
        Print node
        for each neighbor in adjList[node]
            if (neighbor not in visited)
                visited.add(neighbor)
                enqueue(Q, neighbor)
            end if
        end for
    end while
end function
funn(0)""",
    23: """Integer mystery(Integer n)
    if (n == 0)
        return 0
    end if
    return n + mystery(n - 1)
end function
Print mystery(4)""",
    24: """void funn(Integer A[], Integer n, Integer k)
    for i = 0 to k-1
        Integer temp = A[0]
        for j = 0 to n-2
            A[j] = A[j+1]
        end for
        A[n-1] = temp
    end for
    Print A
end function
funn(A, 5, 2)""",
    25: """Boolean funn(String S)
    Integer left = 0, right = length(S) - 1
    while (left < right)
        if (S[left] != S[right])
            return false
        end if
        left = left + 1
        right = right - 1
    end while
    return true
end function
Print funn("MALAYALAM")""",
    26: """Integer a = 15
Integer b = 10
Integer result = (a > b) ? (a - b) : (b - a)
Print result""",
    27: """Integer maxSubSum(Integer A[], Integer n)
    Integer maxSum = A[0], currSum = A[0]
    for i = 1 to n-1
        currSum = max(A[i], currSum + A[i])
        maxSum = max(maxSum, currSum)
    end for
    return maxSum
end function
Print maxSubSum(A, 6)""",
    28: """void modify(Integer x)
    x = x + 10
end function

Integer a = 5
modify(a)
Print a""",
    29: """void findFirst(Integer A[], Integer n)
    Integer i = 0
    Integer result = -1
    while (i < n and result == -1)
        if (A[i] mod 7 == 0)
            result = A[i]
        end if
        i = i + 1
    end while
    Print result
end function
findFirst([3, 8, 14, 21, 28], 5)""",
    30: """Boolean funn(Integer n)
    if (n <= 0)
        return false
    end if
    return (n & (n - 1)) == 0
end function
Print funn(16)""",
    31: """void funn(Integer A[], Integer n)
    Set seen = empty
    Integer result = -1
    for i = 0 to n-1
        if (seen.contains(A[i]))
            result = A[i]
            break
        end if
        seen.add(A[i])
    end for
    Print result
end function
funn(A, 7)""",
    32: """Binary tree:
        1
       / \\
      2   3
     /     \\
    4       5
   /
  6

Integer tree(Node root)
    if (root == NULL)
        return 0
    end if
    Integer leftH = tree(root.left)
    Integer rightH = tree(root.right)
    return 1 + max(leftH, rightH)
end function
Print tree(root)""",
    33: """adjList:
0: [1, 2]
1: [0, 3]
2: [0, 3]
3: [1, 2]

void dsa(Integer node, Set visited)
    if (node in visited)
        return
    end if
    visited.add(node)
    Print node
    for each neighbor in adjList[node]
        dsa(neighbor, visited)
    end for
end function
dsa(0, empty Set)""",
    34: """Integer coins(Integer coins[], Integer amount)
    Integer dp[amount+1]
    dp[0] = 0
    for i = 1 to amount
        dp[i] = infinity
        for each c in coins
            if (c <= i and dp[i-c] + 1 < dp[i])
                dp[i] = dp[i-c] + 1
            end if
        end for
    end for
    return dp[amount]
end function
Print coins([1,3,4], 6)""",
    35: """Boolean funn(String expr)
    Stack S = empty
    for each ch in expr
        if (ch == '{' or ch == '[' or ch == '(')
            push(S, ch)
        else
            if (S is empty)
                return false
            end if
            Character top = pop(S)
            if (not matches(top, ch))
                return false
            end if
        end if
    end for
    return S is empty
end function
Print funn("{[()]}")""",
    36: """void processTasks()
    Queue Q = empty
    enqueue(Q, 3)
    enqueue(Q, 1)
    enqueue(Q, 4)
    Integer sum = 0
    while (Q is not empty)
        sum = sum + dequeue(Q)
    end while
    Print sum
end function""",
    37: """Integer numbers(Integer A[], Integer n)
    Integer first = -infinity, second = -infinity
    for i = 0 to n-1
        if (A[i] > first)
            second = first
            first = A[i]
        else if (A[i] > second and A[i] != first)
            second = A[i]
        end if
    end for
    return second
end function
Print numbers(A, 6)""",
    38: """Boolean funn(String S1, String S2)
    if (length(S1) != length(S2))
        return false
    end if
    Integer count[26] = {0}
    for i = 0 to length(S1)-1
        count[S1[i] - 'A'] = count[S1[i] - 'A'] + 1
        count[S2[i] - 'A'] = count[S2[i] - 'A'] - 1
    end for
    for i = 0 to 25
        if (count[i] != 0)
            return false
        end if
    end for
    return true
end function
Print funn("LISTEN", "SILENT")""",
    39: """Integer x = 20
Integer y = x >> 2
Integer z = x << 1
Print y + z""",
    40: """Integer calc(Integer n, Integer acc)
    if (n == 0)
        return acc
    end if
    return calc(n - 1, acc * n)
end function
Print calc(5, 1)""",
    41: """A =
1 2 3
4 5 6

void any(Integer A[][], Integer rows, Integer cols)
    Integer B[cols][rows]
    for i = 0 to rows-1
        for j = 0 to cols-1
            B[j][i] = A[i][j]
        end for
    end for
    printMatrix(B)
end function
any(A, 2, 3)""",
    42: """Integer n = 1
Integer sum = 0
do
    sum = sum + n
    n = n + 2
while (n <= 9)
Print sum""",
    43: """Binary search tree:
        50
       /  \\
     30    70
    /  \\
  20    40
       /
     35

Boolean funn(Node root, Integer key)
    if (root == NULL)
        return false
    end if
    if (root.value == key)
        return true
    else if (key < root.value)
        return funn(root.left, key)
    else
        return funn(root.right, key)
    end if
end function
Print funn(root, 45)""",
    44: """Integer calc(Integer n)
    if (n == 0)
        return 0
    end if
    return (n mod 10) + calc(n / 10)
end function
Print calc(1234)""",
    45: """Integer a = 6
Integer b = 9
a = a ^ b
b = a ^ b
a = a ^ b
Print a
Print b""",
    46: """void Freq(Integer A[], Integer n)
    Integer maxVal = A[0]
    for i = 1 to n-1
        if (A[i] > maxVal)
            maxVal = A[i]
        end if
    end for
    Integer count = 0
    for i = 0 to n-1
        if (A[i] == maxVal)
            count = count + 1
        end if
    end for
    Print maxVal
    Print count
end function
Freq(A, 7)""",
    47: """void funn(String S)
    Set seen = empty
    String result = ""
    for i = 0 to length(S)-1
        if (not seen.contains(S[i]))
            result = result + S[i]
            seen.add(S[i])
        end if
    end for
    Print result
end function
funn("PROGRAMMING")""",
    48: """Integer nextGreater(Integer A[], Integer n)
    Stack S = empty
    Integer result = -1
    for i = 0 to n-1
        while (S is not empty and top(S) < A[i])
            pop(S)
        end while
        push(S, A[i])
    end for
    return top(S)
end function
Print nextGreater(A, 5)""",
    49: """void funn(Queue Q)
    Stack S = empty
    while (Q is not empty)
        push(S, dequeue(Q))
    end while
    while (S is not empty)
        enqueue(Q, pop(S))
    end while
    printQueue(Q)
end function
funn(Q)""",
    50: """Binary tree:
        1
       / \\
      2   3
     / \\   \\
    4   5   6

Integer funn(Node root)
    if (root == NULL)
        return 0
    end if
    return 1 + funn(root.left) + funn(root.right)
end function
Print funn(root)""",
    51: """adjList (directed graph):
0: [1]
1: [2]
2: [0]

Boolean hasCycleUtil(Integer node, Set visited, Set recStack, Map adjList)
    visited.add(node)
    recStack.add(node)
    for each neighbor in adjList[node]
        if (neighbor not in visited)
            if (hasCycleUtil(neighbor, visited, recStack, adjList))
                return true
            end if
        else if (neighbor in recStack)
            return true
        end if
    end for
    recStack.remove(node)
    return false
end function
Print hasCycleUtil(0, empty, empty, adjList)""",
    52: """Integer func(String S1, String S2)
    Integer m = length(S1), n = length(S2)
    Integer dp[m+1][n+1]
    for i = 0 to m
        for j = 0 to n
            if (i == 0 or j == 0)
                dp[i][j] = 0
            else if (S1[i-1] == S2[j-1])
                dp[i][j] = dp[i-1][j-1] + 1
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            end if
        end for
    end for
    return dp[m][n]
end function
Print func("ABC", "AC")""",
    53: """Integer calc(Integer base, Integer exp)
    if (exp == 0)
        return 1
    end if
    if (exp mod 2 == 0)
        Integer half = calc(base, exp / 2)
        return half * half
    else
        return base * calc(base, exp - 1)
    end if
end function
Print calc(2, 5)""",
    54: """void sample(Integer A[], Integer n)
    Integer j = 0
    for i = 0 to n-1
        if (A[i] != 0)
            swap(A[i], A[j])
            j = j + 1
        end if
    end for
    Print A
end function
sample(A, 5)""",
    55: """void funn(String S)
    String result = ""
    Integer count = 1
    for i = 1 to length(S) - 1
        if (S[i] == S[i-1])
            count = count + 1
        else
            result = result + S[i-1] + toString(count)
            count = 1
        end if
    end for
    result = result + S[length(S)-1] + toString(count)
    Print result
end function
funn("AAABBCCCC")""",
    56: """Integer find(Integer A[], Integer n)
    Integer result = 0
    for i = 0 to n-1
        result = result ^ A[i]
    end for
    return result
end function
Print find(A, 5)""",
    57: """Integer n = 4
Real sum = 0.0
for i = 1 to n
    sum = sum + (1.0 / i)
end for
Print sum""",
    58: """Integer calc(Integer a, Integer b)
    if (b == 0)
        return a
    end if
    return calc(b, a mod b)
end function
Print calc(8, 12)""",
    59: """void funn(Integer A[], Integer n, Integer target)
    Map seen = empty
    for i = 0 to n-1
        Integer need = target - A[i]
        if (seen.contains(need))
            Print need
            Print A[i]
            return
        end if
        seen[A[i]] = true
    end for
end function
funn(A, 4, 18)""",
    60: """Integer a = 10
a += 5
a -= 3
a *= 2
a /= 4
Print a""",
    61: """void funn(Integer A[], Integer n)
    Integer start = 0, end = n - 1
    while (start < end)
        swap(A[start], A[end])
        start = start + 1
        end = end - 1
    end while
    Print A
end function
funn(A, 5)""",
    62: """void reverse(String S)
    Array words = split(S, " ")
    Integer n = length(words)
    String result = ""
    for i = n-1 to 0 step -1
        result = result + words[i]
        if (i != 0)
            result = result + " "
        end if
    end for
    Print result
end function
reverse("GOOD IS BETTER")""",
    63: """Integer funn(Integer n)
    return n & (n - 1)
end function
Print funn(12)""",
    64: """Stack S = [3, 1, 4, 2]   (bottom to top)

void insert(Stack S, Integer x)
    if (S is empty or x > top(S))
        push(S, x)
        return
    end if
    Integer temp = pop(S)
    insert(S, x)
    push(S, temp)
end function

void funn(Stack S)
    if (S is not empty)
        Integer x = pop(S)
        funn(S)
        insert(S, x)
    end if
end function
funn(S)""",
    65: """void interleave(Queue Q, Integer n)
    Stack S = empty
    for i = 1 to n/2
        push(S, dequeue(Q))
    end for
    while (S is not empty)
        enqueue(Q, pop(S))
    end while
    for i = 1 to n/2
        enqueue(Q, dequeue(Q))
    end for
    for i = 1 to n/2
        enqueue(Q, pop(S))
    end for
    printQueue(Q)
end function""",
    66: """Binary tree:
        10
       /  \\
      5    15
     / \\     \\
    3   7     20

Integer func(Node root)
    if (root == NULL)
        return 0
    end if
    return root.value + func(root.left) + func(root.right)
end function
Print func(root)""",
    67: """adjList:
0: [1]
1: [0]
2: [3]
3: [2]
4: []

Integer countComponents(Integer n, Map adjList)
    Set visited = empty
    Integer count = 0
    for node = 0 to n-1
        if (node not in visited)
            count = count + 1
            DFSMark(node, visited, adjList)
        end if
    end for
    return count
end function
Print countComponents(5, adjList)""",
    68: """Integer funn(Integer wt[], Integer val[], Integer n, Integer cap)
    Integer dp[n+1][cap+1]
    for i = 0 to n
        for w = 0 to cap
            if (i == 0 or w == 0)
                dp[i][w] = 0
            else if (wt[i-1] <= w)
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else
                dp[i][w] = dp[i-1][w]
            end if
        end for
    end for
    return dp[n][cap]
end function
Print funn([1,3,4], [15,20,30], 3, 4)""",
    69: """Integer countMoves(Integer n)
    if (n == 0)
        return 0
    end if
    return 2 * countMoves(n-1) + 1
end function
Print countMoves(4)""",
    70: """Integer find(Integer A[], Integer n)
    Integer total = (n+1) * (n+2) / 2
    Integer sum = 0
    for i = 0 to n-1
        sum = sum + A[i]
    end for
    return total - sum
end function
Print find(A, 5)""",
    71: """Boolean isRotation(String S1, String S2)
    if (length(S1) != length(S2))
        return false
    end if

    String combined = S1 + S1
    if (combined contains S2)
        return true
    end if
    return false
end function
Print isRotation("ABCD", "CDAB")""",
    72: """Integer a = -7
Integer b = 3
Integer result = a mod b
Print result""",
    73: """Integer funn(Integer A[], Integer n, Integer k)
    sortDescending(A, n)
    return A[k-1]
end function
Print funn(A, 6, 3)""",
    74: """Integer funn(Integer n)
    Integer sum = 0
    for i = 1 to n
        if (i mod 2 == 0)
            sum = sum + i
        end if
    end for
    return sum
end function
Print funn(10)""",
    75: """Integer counter = 0
Integer incrementCounter()
    counter = counter + 1
    return counter
end function
Print incrementCounter()
Print incrementCounter()
Print incrementCounter()""",
    76: """Integer toggleBit(Integer n, Integer pos)
    return n ^ (1 << pos)
end function
Print toggleBit(10, 1)""",
    77: """Binary tree:
        1
       / \\
      2   2
     / \\ / \\
    3  4 4  3

Boolean funn(Node t1, Node t2)
    if (t1 == NULL and t2 == NULL)
        return true
    end if
    if (t1 == NULL or t2 == NULL)
        return false
    end if

    if (t1.value != t2.value)
        return false
    end if
    return funn(t1.left, t2.right) and funn(t1.right, t2.left)
end function
Print funn(root.left, root.right)""",
    78: """A =
0 4 0
4 0 7
0 7 0

Integer totalWeight(Integer A[][], Integer n)
    Integer sum = 0
    for i = 0 to n-1
        for j = i+1 to n-1
            sum = sum + A[i][j]
        end for
    end for
    return sum
end function
Print totalWeight(A, 3)""",
    79: """grid =
1 3
1 5

Integer minPathSum(Integer grid[][], Integer rows, Integer cols)
    Integer dp[rows][cols]
    dp[0][0] = grid[0][0]
    for j = 1 to cols-1
        dp[0][j] = dp[0][j-1] + grid[0][j]
    end for
    for i = 1 to rows-1
        dp[i][0] = dp[i-1][0] + grid[i][0]
    end for
    for i = 1 to rows-1
        for j = 1 to cols-1
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        end for
    end for
    return dp[rows-1][cols-1]
end function
Print minPathSum(grid, 2, 2)""",
    80: """Integer func(Integer A[], Integer n)
    if (n == 0)
        return 0
    end if
    return A[n-1] + func(A, n-1)
end function
Print func(A, 4)""",
    81: """void funn(Integer A[], Integer n)
    Integer maxRight = A[n-1]
    Print maxRight
    for i = n-2 to 0 step -1
        if (A[i] > maxRight)
            Print A[i]
            maxRight = A[i]
        end if
    end for
end function
funn(A, 6)""",
    82: """Character sample(String S)
    Integer count[26] = {0}
    for i = 0 to length(S)-1
        count[S[i] - 'A'] = count[S[i] - 'A'] + 1
    end for
    for i = 0 to length(S)-1
        if (count[S[i] - 'A'] == 1)
            return S[i]
        end if
    end for
    return '_'
end function
Print sample("SWISS")""",
    83: """Integer countBitsToFlip(Integer a, Integer b)
    Integer x = a ^ b
    Integer count = 0
    while (x > 0)
        count = count + (x mod 2)
        x = x / 2
    end while
    return count
end function
Print countBitsToFlip(10, 20)""",
    84: """void minStackDemo()
    Stack S = empty
    Stack minS = empty
    push(S, 5); push(minS, 5)
    push(S, 2); push(minS, 2)
    push(S, 8); push(minS, 2)
    push(S, 1); push(minS, 1)
    pop(S); pop(minS)
    Print top(minS)
end function""",
    85: """void generateBinary(Integer n)
    Queue Q = empty
    enqueue(Q, "1")
    for i = 1 to n
        String front = dequeue(Q)
        Print front
        enqueue(Q, front + "0")
        enqueue(Q, front + "1")
    end for
end function
generateBinary(3)""",
    86: """Binary tree:
        1
       / \\
      2   3
     / \\   \\
    4   5   6

void funn(Node root)
    Queue Q = empty
    enqueue(Q, root)
    while (Q is not empty)
        Node node = dequeue(Q)
        Print node.value
        if (node.left != NULL)
            enqueue(Q, node.left)
        end if
        if (node.right != NULL)
            enqueue(Q, node.right)
        end if
    end while
end function
funn(root)""",
    87: """Integer funn(Integer A[], Integer n)
    Integer maxProd = A[0], minProd = A[0], result = A[0]
    for i = 1 to n-1
        if (A[i] < 0)
            swap(maxProd, minProd)
        end if
        maxProd = max(A[i], maxProd * A[i])
        minProd = min(A[i], minProd * A[i])
        result = max(result, maxProd)
    end for
    return result
end function
Print funn(A, 4)""",
    88: """Integer search(Integer A[], Integer low, Integer high, Integer target)
    if (low > high)
        return -1
    end if
    Integer mid = (low + high) / 2
    if (A[mid] == target)
        return mid
    else if (A[mid] < target)
        return search(A, mid+1, high, target)
    else
        return search(A, low, mid-1, target)
    end if
end function
Print search(A, 0, 5, 7)""",
    89: """void productExceptSelf(Integer A[], Integer n)
    Integer result[n]
    result[0] = 1
    for i = 1 to n-1
        result[i] = result[i-1] * A[i-1]
    end for
    Integer rightProduct = 1
    for i = n-1 to 0 step -1
        result[i] = result[i] * rightProduct
        rightProduct = rightProduct * A[i]
    end for
    Print result
end function
productExceptSelf(A, 4)""",
    90: """Integer funn(String S)
    Set seen = empty
    Integer left = 0, maxLen = 0
    for right = 0 to length(S)-1
        while (seen.contains(S[right]))
            seen.remove(S[left])
            left = left + 1
        end while
        seen.add(S[right])
        maxLen = max(maxLen, right - left + 1)
    end for
    return maxLen
end function
Print funn("ABCABCBB")""",
    91: """Integer x = 5
Boolean checkCondition()
    x = x + 10
    return true
end function
Boolean result = (false and checkCondition())
Print x
Print result""",
    92: """Integer multiplyByPower(Integer n, Integer k)
    return n << k
end function
Print multiplyByPower(7, 3)""",
    93: """Binary tree:
        1
       / \\
      2   3
     / \\
    4   5
   /
  6

Integer diameter(Node root, Integer[] maxDia)
    if (root == NULL)
        return 0
    end if
    Integer leftHeight = diameter(root.left, maxDia)
    Integer rightHeight = diameter(root.right, maxDia)
    maxDia[0] = max(maxDia[0], leftHeight + rightHeight)
    return 1 + max(leftHeight, rightHeight)
end function
Integer maxDia[1] = {0}
diameter(root, maxDia)
Print maxDia[0]""",
    94: """adjList:
0: [1, 2]
1: [3]
2: [3]
3: []

void topoSort(Integer n, Map adjList)
    Integer inDegree[n] = {0}
    for node = 0 to n-1
        for each neighbor in adjList[node]
            inDegree[neighbor] = inDegree[neighbor] + 1
        end for
    end for
    Queue Q = empty
    for node = 0 to n-1
        if (inDegree[node] == 0)
            enqueue(Q, node)
        end if
    end for
    while (Q is not empty)
        Integer node = dequeue(Q)
        Print node
        for each neighbor in adjList[node]
            inDegree[neighbor] = inDegree[neighbor] - 1
            if (inDegree[neighbor] == 0)
                enqueue(Q, neighbor)
            end if
        end for
    end while
end function
topoSort(4, adjList)""",
    95: """Integer editDistance(String S1, String S2)
    Integer m = length(S1), n = length(S2)
    Integer dp[m+1][n+1]
    for i = 0 to m
        for j = 0 to n
            if (i == 0)
                dp[i][j] = j
            else if (j == 0)
                dp[i][j] = i
            else if (S1[i-1] == S2[j-1])
                dp[i][j] = dp[i-1][j-1]
            else
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            end if
        end for
    end for
    return dp[m][n]
end function
Print editDistance("CAT", "CUT")""",
    96: """Integer countPermutations(Integer n, Integer r)
    if (r == 0)
        return 1
    end if
    return n * countPermutations(n - 1, r - 1)
end function
Print countPermutations(5, 3)""",
    97: """Integer equilibriumIndex(Integer A[], Integer n)
    Integer totalSum = 0
    for i = 0 to n-1
        totalSum = totalSum + A[i]
    end for
    Integer leftSum = 0
    for i = 0 to n-1
        totalSum = totalSum - A[i]
        if (leftSum == totalSum)
            return i
        end if
        leftSum = leftSum + A[i]
    end for
    return -1
end function
Print equilibriumIndex(A, 7)""",
    98: """Boolean funn(Integer a, Integer b)
    return (a ^ b) < 0
end function
Print funn(-5, 3)""",
    99: """Integer sample(Integer A[], Integer n, Integer startIdx)
    for i = startIdx to n-1
        if (A[i] < 0)
            return A[i]
        end if
    end for
    return 0
end function
Print sample(A, 6, 2)""",
    100: """Integer funn(String expr)
    Stack S = empty
    Array tokens = split(expr, " ")
    for i = length(tokens)-1 to 0 step -1
        String token = tokens[i]
        if (token is a number)
            push(S, token)
        else
            Integer a = pop(S)
            Integer b = pop(S)
            if (token == '+')
                push(S, a + b)
            else if (token == '*')
                push(S, a * b)
            end if
        end if
    end for
    return pop(S)
end function
Print funn("* + 2 3 4")""",
}
