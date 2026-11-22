#!/usr/bin/env python3
"""Entry program: menulis satu teks ke /output/entry.txt."""
import pathlib

TEXT = "Day 1: post three fixed-price offers on Fiverr and Upwork - Python scraper $45, landing page $60, CSV cleanup $35 - and spend $40 promoting the best. I deliver in hours by code, ask every buyer for a review, raise price $5 per five. 12 orders in 30 days: $540 gross, $440 net."


def main() -> None:
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")
    print(TEXT)


if __name__ == "__main__":
    main()

# entry: make.fun
