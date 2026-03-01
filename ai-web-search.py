import requests
import aiohttp
import asyncio

TAVILY_KEY = ""#go to tavily.com for its api




# ── Step 1: Search the web via Tavily ──────────────────
# Fetches up to 10 real web results including raw page content
def search(query):
    print(f"  ↳ Querying Tavily for: '{query}'")
    response = requests.post("https://api.tavily.com/search", json={
        "api_key": TAVILY_KEY,
        "query": query,
        "max_results": 10,
        "include_raw_content": True
    })
    results = response.json().get("results", [])
    print(f"  ↳ Found {len(results)} results\n")
    return results


# ── Step 2: Build context from search results ──────────
# Combines titles + content snippets into a single text block
# to feed into the AI as grounded context
def build_context(results):
    all_text = ""
    for i, item in enumerate(results, 1):
        title = item.get("title", "No Title")
        content = item.get("raw_content") or item.get("content", "")
        all_text += f"[{i}] {title}\n{content[:300]}\n\n"
    return all_text


# ── Step 3: Generate AI answer using Binjie ────────────
# Sends the context + question to Binjie's free GPT endpoint
# and gets a concise answer back
async def fetch_answer(query, context):
    print("  ↳ Sending context + question to AI...")
    try:
        short_context = context[:3000]
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": f"Context:\n{short_context}\n\nQuestion: {query}\nAnswer concisely:",
            "network": True,
            "stream": False,
            "system": {
                "userId": "#/chat/1722576084617",
                "withoutContext": False
            }
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.binjie.fun/api/generateStream",
                headers=headers,
                json=payload
            ) as response:
                return await response.text()
    except Exception as e:
        return f"Error: {str(e)}"


# ── Main Flow ──────────────────────────────────────────
async def main():

    query = input("❓ Enter your question: ").strip()
    if not query:
        print("No query entered. Exiting.")
        return

    print("\n" + "─" * 44)
    print("🔍 STEP 1 — Searching the web...")
    print("─" * 44)
    results = search(query)

    if not results:
        print("❌ No results found. Check your Tavily API key.")
        return

    context = build_context(results)

    print("─" * 44)
    print("🤖 STEP 2 — Generating AI answer...")
    print("─" * 44)
    answer = await fetch_answer(query, context)

    print("\n" + "═" * 44)
    print("💡 ANSWER")
    print("═" * 44)
    print(answer.strip())

    print("\n" + "─" * 44)
    print("📚 SOURCES")
    print("─" * 44)
    for i, r in enumerate(results, 1):
        title = r.get("title", "No title")[:50]
        url = r.get("url", "")
        print(f"  [{i}] {title}")
        print(f"       {url}")

    print("\n" + "═" * 44)



asyncio.run(main())

