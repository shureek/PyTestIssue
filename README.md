# PyTestIssue
I'm trying to use pytest for unit testing, but I cannot solve import module problem. When test module is loading by pytest it cannot import modules from parent folders.
Here I have main.py, which imports mylib/mat, which loads baselib successfully.

    > python main.py
    3 + 5 = 8
	3 + 5 = 13

But when I run pytest tests/test_mylib.py cannot load baselib!

	> pytest
	============================= test session starts =============================
	platform win32 -- Python 3.5.2, pytest-3.0.5, py-1.4.31, pluggy-0.4.0
	rootdir: D:\Documents\Development\Python\PyTestIssue, inifile:
	collected 0 items / 1 errors
	
	=================================== ERRORS ====================================
	____________________ ERROR collecting tests/test_mylib.py _____________________
	ImportError while importing test module 'D:\Documents\Development\Python\PyTestIssue\tests\test_mylib.py'.
	Hint: make sure your test modules/packages have valid Python names.
	Traceback:
	tests\test_mylib.py:1: in <module>
    	import baselib
	E   ImportError: No module named 'baselib'
	!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!
	=========================== 1 error in 0.18 seconds ===========================

What am I doing wrong?