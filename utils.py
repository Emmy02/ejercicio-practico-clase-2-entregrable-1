import requests
from datetime import datetime, timedelta
BASE_URL = "http://localhost:8000"

def assert_ok(res: requests.Response, expected_status: int = 200):
    assert res.status_code == expected_status, (
        f"Expected {expected_status}, got {res.status_code}. Body: {res.text}"
    )

def print_response(label: str, response: requests.Response):
    print(f"\n[{response.status_code}] {label}")
    if response.status_code == 204:
        print("  ✅ Deleted successfully")
    elif response.ok:
        print(f"  ✅ {response.json()}")
    else:
        try:
            detail = response.json().get('detail', response.text)
        except Exception:
            detail = response.text if response.text else "Empty response — check server logs"
        print(f"  ❌ Error: {detail}")

