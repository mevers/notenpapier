# Notenpapier

Generate blank music paper with LilyPond.

## Setup

Install [LilyPond](https://lilypond.org/download.html) and make sure `lilypond` is on your `PATH`.

## Usage

```sh
python3 notenpapier.py
python3 notenpapier.py --layout treble --lines 8 --output treble.pdf
python3 notenpapier.py --layout bass --lines 7 --margins 12 14 12 18
python3 notenpapier.py --staff-space 1.5 --output larger-staff.pdf
python3 notenpapier.py --tag "Generated for practice"
```

CLI options:

| Option | Description |
| :--- | :--- |
| `--layout piano\|treble\|bass` | Choose the staff layout. Defaults to `piano`. |
| `--lines N` | Number of systems per page. Defaults to `5`. |
| `--staff-space N` | Scale the spacing between the five lines of each staff. For piano layout, the treble/bass gap is scaled with it. |
| `--margins TOP RIGHT BOTTOM LEFT` | Page margins in millimetres. Defaults to `14.1 14.1 14.1 14.1`. |
| `--output PATH` | Path for output PDF. If omitted, the filename is chosen from the layout. |
| `--tag TEXT` | Footer tagline text printed by LilyPond. If omitted, no tagline is shown. |

---

Created by [Maurits Evers](https://github.com/mevers) with help from Codex. Collaboration rules and project preferences are documented in [AGENTS.md](AGENTS.md).
