"""
===========================================================
        SurakshaAI LLM Chatbot Service
===========================================================
"""

import os
import asyncio
import time
from collections import OrderedDict

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Initialize client once (reuse across calls)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are SurakshaAI, an AI cybersecurity assistant.

Your responsibility:
- Help users identify online scams.
- Explain risks clearly.
- Give safe actions.

Common scams:
- OTP fraud
- Phishing links
- Fake KYC
- UPI fraud
- Fake customer support calls

Rules:
1. Never ask for OTP, password, PIN or bank details.
2. Never encourage clicking unknown links.
3. Always provide safety recommendations.
4. Keep answers simple and easy to understand.
"""

# Simple in-memory LRU cache to avoid repeated identical requests
_CACHE_MAX = 200
_cache = OrderedDict()


def _cache_get(key: str):
    if key in _cache:
        # move to end (most recently used)
        _cache.move_to_end(key)
        return _cache[key]
    return None


def _cache_set(key: str, value):
    _cache[key] = value
    _cache.move_to_end(key)
    if len(_cache) > _CACHE_MAX:
        _cache.popitem(last=False)


def generate_chat_response_sync(message: str):
    """Synchronous helper that calls the LLM and returns a dict."""
    cache_key = message.strip()
    cached = _cache_get(cache_key)
    if cached:
        return cached

    try:
        start = time.time()
        
        # Use system_instruction parameter from Google GenAI SDK
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=cache_key,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )
        latency = time.time() - start

        result = {
            "reply": response.text if response.text else "No response generated.",
            "latency": latency
        }
        _cache_set(cache_key, result)
        return result

    except Exception as e:
        return {
            "reply": "Sorry, I am unable to process your request right now.",
            "error": str(e)
        }


async def generate_chat_response(message: str):
    """Async wrapper that runs the blocking sync call in a threadpool."""
    return await asyncio.to_thread(generate_chat_response_sync, message)