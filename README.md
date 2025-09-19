# Greet based on time

```python
def _greeting_from_time(local_time_str: str | None) -> str:
    """
    Parse a local time string (various formats) and return a part-of-day greeting.
    Handles AM/PM and 24h times. Fallback: 'Hello'.
    """
    import re
    from datetime import datetime

    if not local_time_str:
        return "Hello"

    try:
        hour = None

        # --- 1) Regex extraction (handles '09AM', '9:15 pm', '21:30', etc.) ---
        match = re.search(r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)?", local_time_str, re.I)
        if match:
            hour = int(match.group(1))
            ampm = (match.group(3) or "").upper()

            if ampm == "PM" and hour != 12:
                hour += 12
            if ampm == "AM" and hour == 12:
                hour = 0

        # --- 2) If regex didn’t yield, try ISO format (e.g., '2025-09-19T20:15:00') ---
        if hour is None:
            try:
                dt = datetime.fromisoformat(local_time_str.strip())
                hour = dt.hour
            except Exception as iso_ex:
                print(f"{iso_ex}")

        # --- 3) If still None, last fallback: try %H:%M ---
        if hour is None:
            try:
                dt = datetime.strptime(local_time_str.strip(), "%H:%M")
                hour = dt.hour
            except Exception as hm_ex:
                print(f"{hm_ex}")

        # --- 4) If we got an hour, map it ---
        if hour is not None:
            if 5 <= hour < 12:
                return "Good morning"
            elif 12 <= hour < 17:
                return "Good afternoon"
            elif 17 <= hour < 22:
                return "Good evening"
            else:
                return "Hello"
    except Exception as ex:
        print(f"{ex}")

    # Absolute fallback
    return "Hello"
```


