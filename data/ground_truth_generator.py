"""
Ground truth generator.
Generates GT markdown by taking Engine A's content and appending the
Site Navigation and Footer sections from Engine C's output.
PDF pages are excluded from the nav/footer append since they have no
site chrome.

Run via: python data/ground_truth_generator.py <cache_a_path> <cache_c_path> [--pdf]
"""
import pathlib
import sys


def _extract_nav_footer(text: str) -> str:
    """Extract the ## Site Navigation and ## Footer sections from Engine C output."""
    lines = text.split("\n")
    start = None
    end = None
    past_footer = False

    for i, line in enumerate(lines):
        if line.strip() == "## Site Navigation":
            start = i
        if line.strip() == "## Footer":
            past_footer = True
        elif past_footer and line.startswith("## "):
            end = i
            break

    if start is None:
        return ""

    section_lines = lines[start:end]
    while section_lines and not section_lines[-1].strip():
        section_lines.pop()

    return "\n".join(section_lines)


def generate(cache_a_path: str, cache_c_path: str, is_pdf: bool = False) -> str:
    engine_a = pathlib.Path(cache_a_path).read_text().strip()

    if is_pdf:
        return engine_a

    engine_c = pathlib.Path(cache_c_path).read_text()
    nav_footer = _extract_nav_footer(engine_c)
    if nav_footer:
        return engine_a + "\n\n" + nav_footer
    return engine_a


if __name__ == "__main__":
    pdf_flag = "--pdf" in sys.argv
    print(generate(sys.argv[1], sys.argv[2], is_pdf=pdf_flag))
