# Testing Checklist

Run `python main.py` and verify each case. Record actual results before marking any test as passed.

| # | Test | Input / action | Expected result | Actual result |
|---|---|---|---|---|
| 1 | Normal calculation | Mathematics (3 units, 1.75), Programming (3, 1.50), English (3, 2.00) | Total units 9; weighted total 15.75; GWA 1.75 | Not run |
| 2 | One subject | One subject with 3 units and grade 2.00 | GWA 2.00 | Not run |
| 3 | Empty name | Press Enter at a required text prompt | Program asks again | Not run |
| 4 | Invalid units text | Enter `abc` for units | Program asks for a whole number | Not run |
| 5 | Non-positive units | Enter `0` or `-2` for units | Program asks for a number greater than zero | Not run |
| 6 | Grade below range | Enter `0.75` | Program rejects the grade | Not run |
| 7 | Grade above range | Enter `5.25` | Program rejects the grade | Not run |
| 8 | Invalid increment | Enter `1.10` | Program rejects the grade | Not run |

The test table intentionally says `Not run` until a person performs the interactive checks.
