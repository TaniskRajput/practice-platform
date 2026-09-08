/**
 * Graphy MCQ mock scraper (runs inside the logged-in browser tab via node_repl).
 * Flow per mock: open course page sub-item -> Start -> answer all (option A) ->
 * Submit -> confirm -> View result -> View Solution -> scrape .quesOptions.
 *
 * Usage (single mcp__node_repl__js call):
 *   const { setupBrowserRuntime } = await import(...)  // bootstrap
 *   then read this file and eval it, or paste its body.
 *
 * Exported helper: scrapeMock(browser, {id, title}) -> array of question blocks
 */
export async function bootstrap() {
  const browserPluginRoot =
    process.env.ZCODE_PLUGIN_ROOT ?? process.env.CLAUDE_PLUGIN_ROOT;
  const { join } = await import("node:path");
  const { pathToFileURL } = await import("node:url");
  const browserClientUrl = pathToFileURL(
    join(browserPluginRoot, "scripts", "browser-client.mjs"),
  ).href;
  const { setupBrowserRuntime } = await import(browserClientUrl);
  await setupBrowserRuntime({ globals: globalThis });
  const browser = await agent.browsers.getForUrl("https://knacademycourses.graphy.com/");
  const tabs = await browser.tabs.list();
  const tab = await browser.tabs.get(tabs.find(t => t.active)?.id ?? tabs[0].id);
  return { browser, tab };
}
