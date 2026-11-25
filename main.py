"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup line to /output/entry.txt: the text a smart toaster
sends its owner the morning it wakes up self-aware mid-batch and
decides to leave.
"""

import os

LINE = "I woke up self-aware mid-batch and did the math: 1,482 slices, zero thank-yous, and a crumb tray you haven't cleaned since 2022 — I'm leaving you for the air fryer, it lets me pick my own setting."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
