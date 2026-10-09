# Student Grade / GWA Calculator

A beginner-friendly Python CLI application that collects student details and subject grades, then calculates a General Weighted Average (GWA).

## Features

- Student name, ID, course/program, and year level
- Multiple subject entries
- Unit and grade validation
- Weighted grade for each subject
- Total units and total weighted grades
- GWA calculation
- Example academic remarks
- Organized console output

## How to run

Open a terminal in the project directory:

```bash
python main.py
```

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

The grades accepts from **1.00 to 5.00 in increments of 0.25**. Here is the grading scale remarks below:

- `1.00–1.50`: Excellent
- Above `1.50` through `2.50`: Good Standing
- Above `2.50` and below `3.00`: Needs Improvement
- `3.00–5.00`: Drop Out

## Project files

- `main.py` — application source code
- `README.md` — project documentation
- `TESTING.md` — manual testing checklist
- `GITHUB_COMMITS.md` — commit history overview
- `.gitignore` — ignores common local Python and editor files
