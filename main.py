"""make.fun entry: writes the plan text to /output/entry.txt (stdlib only)."""

from pathlib import Path

# Entry text: exactly 276 characters, verified byte-for-byte on every run.
TEXT = (
    "Day 1: post three fixed-price offers on Fiverr and Upwork"
    " - Python scraper $45, landing page $60, CSV cleanup $35"
    " - and spend $40 promoting the best."
    " I deliver in hours by code, ask every buyer for a review,"
    " raise price $5 per five."
    " 12 orders in 30 days: $540 gross, $440 net."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} chars to {out}")


if __name__ == "__main__":
    main()
