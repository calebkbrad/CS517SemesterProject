# CS517SemesterProject
Semester Project done for CS 517. Will implement piecewise linear interpolation and least squares approximation in Python

# linear_interpolation.py Usage

# Requirements
    * Python 3.7

# Sample Execution
If executed with an invalid file name or without command line arguments, like so
```
./linear_interpolation.py
```

The following error message will display
```
Please provide a valid input file
```

If provided a path to a valid input file, like sensors2018.12.26-no-labels.txt as provided in the assignment prompt, like so
```
./linear_interpolation.py sensors2018.12.26-no-labels.txt
```

The following success message should display
```
All Interpolations completed successfully
```
New output files will also be created, containing the calculations for each core.
They will be named output_core_n.txt where n is the number of the core, starting with core 0
