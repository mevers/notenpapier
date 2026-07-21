#!/usr/bin/env python3
import argparse, os  # noqa: E401


p = argparse.ArgumentParser(description="Generate blank music paper.")
p.add_argument("--layout", choices=["piano", "treble", "bass"], default="piano")
p.add_argument("--lines", type=int, default=5)
p.add_argument("--staff-space", type=float)
p.add_argument("--margins", nargs=4, type=float, default=[14.1, 14.1, 14.1, 14.1])
p.add_argument("--output")
p.add_argument("--tag", default="")
a = p.parse_args()

out = a.output or {
    "piano": "notenpapier-piano.pdf",
    "treble": "notenpapier-treble.pdf",
    "bass": "notenpapier-bass.pdf",
}[a.layout]
base = out[:-4] if out.endswith(".pdf") else out
top, right, bottom, left = a.margins
breaks = " ".join(["s1 \\break"] * (a.lines - 1) + ["s1"])
tagline = f'"{a.tag}"' if a.tag else "##f"
staff_space = f"\\magnifyStaff #{a.staff_space} " if a.staff_space is not None else ""
piano_staff_space = f"    \\override StaffGrouper.staff-staff-spacing.basic-distance = #{9 * a.staff_space}\n" if a.staff_space is not None else ""

staff = (
    f"\\new PianoStaff <<"
    f"\\new Staff {{ {staff_space}\\clef treble {breaks} }}"
    f"\\new Staff {{ {staff_space}\\clef bass {breaks} }}"
    f">>"
    if a.layout == "piano"
    else f"\\new Staff {{ {staff_space}\\clef {a.layout} {breaks} }}"
)
ly = f"_notenpapier_{os.getpid()}.ly"

open(ly, "w").write(f"""
\\version "2.24.0"
#(set-default-paper-size "a4")
\\header {{ tagline = {tagline} }}
\\paper {{
  top-margin = {top}\\mm
  right-margin = {right}\\mm
  bottom-margin = {bottom}\\mm
  left-margin = {left}\\mm
  indent = 0\\mm
  systems-per-page = {a.lines}
  last-bottom-spacing.basic-distance = #10
  ragged-last = ##f
  ragged-bottom = ##f
  ragged-last-bottom = ##f
}}
\\layout {{
  \\context {{
    \\Score
    \\remove Bar_number_engraver
  }}
  \\context {{
    \\Staff
    \\omit TimeSignature
    \\omit BarLine
  }}
  \\context {{
    \\PianoStaff
    \\remove Span_bar_engraver
{piano_staff_space}
  }}
}}
\\score {{ {staff} }}
""")

status = os.spawnvp(
    os.P_WAIT,
    "lilypond",
    ["lilypond", "-dno-point-and-click", "-o", base, ly],
)
os.remove(ly)
raise SystemExit(status)
