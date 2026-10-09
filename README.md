# Student Grade / GWA Calculator

A beginner-friendly Python console application that collects student details and subject grades, then calculates a General Weighted Average (GWA).

## Features

- Student name, ID, course/program, and year level
- Multiple subject entries
- Unit and grade validation
- Weighted grade for each subject
- Total units and total weighted grades
- GWA calculation
- Example academic remarks
- Organized console output

## Requirements

- Python 3.9 or later recommended
- No third-party packages required
- Git is optional for running the program, but required for the GitHub workflow

## How to run

Open a terminal in the project directory:

```bash
python main.py
```

On Windows, `py main.py` may be used if `python` is not recognized.

## Formula

For each subject:

`Weighted Grade = Grade × Units`

Then:

**GWA = Total Weighted Grades ÷ Total Units**

Example:

| Subject | Units | Grade | Weighted grade |
|---|---:|---:|---:|
| Mathematics | 3 | 1.75 | 5.25 |
| Programming | 3 | 1.50 | 4.50 |
| English | 3 | 2.00 | 6.00 |
| **Total** | **9** | | **15.75** |

GWA = `15.75 ÷ 9` = **1.75**.

## Grading scale and remarks

The sample accepts grades from **1.00 to 5.00 in increments of 0.25**. Its illustrative remarks are:

- `1.00–1.50`: Excellent
- Above `1.50` through `2.50`: Good Standing
- Above `2.50` and below `3.00`: Needs Improvement
- `3.00–5.00`: At Risk / Review Required

These thresholds are examples only, not an official school policy. Grading rules differ by institution; adjust them to match your school's requirements.

## Project files

- `main.py` — application source code
- `README.md` — project documentation
- `TESTING.md` — manual testing checklist
- `GITHUB_COMMITS.md` — commit history overview
- `.gitignore` — ignores common local Python and editor files

## Testing

See `TESTING.md`. Do not claim a manual test passed until you have actually run it.

## Development history

This repository was built using ten progressive commits. Use `git log --oneline` to inspect the history.

## Limitations

- Console interface only
- No database, API, or GUI
- Student data is not saved after the program closes
- Accuracy depends on correct input and the school's grading policy
