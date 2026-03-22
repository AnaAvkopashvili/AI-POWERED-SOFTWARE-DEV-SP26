import os
import time
from dotenv import load_dotenv
from google import genai

# --- initialization ---
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# --- NOTE!!!: gemini-2.0 model was deprecated and couldn't use, so I switch to 2.5 models ---
MODELS = [
    "gemini-2.5-flash", "gemini-2.5-flash-lite",
]
# Pricing according to https://ai.google.dev/gemini-api/docs/pricing
PRICING = {
    "gemini-2.5-flash":      {"in": 0.30,  "out": 2.50},
    "gemini-2.5-flash-lite": {"in": 0.10, "out": 0.40},
}

PROMPT = (
    """ 
    A snail climbs a 10-meter pole. Each day it climbs 3 meters, each night it slides back 2 meters.
However, on rainy days (every 3rd day starting from day 1), it only climbs 1 meter and slides back 3 meters at night.
How many days does it take to reach the top? Show your work step by step.
"""
)


# --- core logic ---
def estimate_price(model, in_tokens, out_tokens):
    rates = PRICING.get(model, {"in": 0, "out": 0})
    return (in_tokens * rates["in"] + out_tokens * rates["out"]) / 1_000_000


def evaluate(model_name):
    t0 = time.perf_counter()

    res = client.models.generate_content(
        model=model_name,
        contents=PROMPT
    )

    elapsed = (time.perf_counter() - t0) * 1000
    usage = res.usage_metadata

    return {
        "model": model_name,
        "text": res.text,
        "input": usage.prompt_token_count,
        "output": usage.candidates_token_count,
        "total": usage.total_token_count,
        "latency": elapsed,
        "cost": estimate_price(
            model_name,
            usage.prompt_token_count,
            usage.candidates_token_count
        )
    }


# --- run ---
reports = []

for m in MODELS:


    result = evaluate(m)
    print(result["text"])

    print("\nStats snapshot:")
    print(f" tokens -> in: {result['input']}, out: {result['output']}, total: {result['total']}")
    print(f" latency -> {result['latency']:.1f} ms")
    print(f" cost -> ${result['cost']:.6f}")

    reports.append(result)


for r in reports:
    print(f"\n[{r['model']}]")
    print(f"  • Token usage: {r['input']} in / {r['output']} out (total {r['total']})")
    print(f"  • Response time: {r['latency']:.1f} ms")
    print(f"  • Estimated cost: ${r['cost']:.6f}")
