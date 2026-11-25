"""Famous Last Words at 1 Percent - one line, written to /output/entry.txt.

famous last words delivered by a machine, preserved in the least romantic place: the boot log.
"""

from pathlib import Path

ENTRY = (
    "At 1% battery my agent said 'watch this' - words later found carved into the boot log, right before everything went dark."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
