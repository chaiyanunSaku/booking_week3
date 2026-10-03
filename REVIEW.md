Identity: 
Chaiyanun Sakulsaowapakkul 6681299. Worked independently.
AI uses: Github Copilot

Review decision:
In service.py/move_booking, the implementation now excludes the booking being moved before calling has_conflict so now it would not wrongly reject a valid overlapping booking with itself. I reviewed the diff and confirmed it is working as intended (same booking overlap).

Checks: 
Baseline commit: fe48967

Ran 6 tests, OK
uv run --python 3.12 python -m unittest -v test_baseline

Ran 3 tests, FAILED (errors=3)
uv run --python 3.12 python -m unittest -v test_move_smoke

Ran 11 tests, OK (after the implementation)
uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student

Remaining uncertainty: 
I was thinking about tests that check for moving a cancelled booking. The code seems to reject correctly but we don't have the test cases for that yet.
