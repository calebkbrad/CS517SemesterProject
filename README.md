# CS517SemesterProject
Semester Project done for CS 517. Will implement piecewise linear interpolation and least squares approximation in Python

## linear_interpolation.py Usage

### Requirements
    * Python 3.7

### Sample Execution
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


## least_squares.py Usage

### Requirements
    * Python 3.7

### Sample Execution
If executed with an invalid file name or without command line arguments, like so 
```
./least_squares.py
```
The following error message will display
```
Please provide a valid input file
```

If provided a path to a valid input file, like sensors2018.12.26-no-labels.txt as provided in the assignment prompt, like so
```
./least_squares.py sensors2018.12.26-no-labels.txt
```
The results of all least squares approximation calculations will be output to the console like so
```
     0 <= x <  35610; y_0      =       77.1459 +    -0.0001x; least squares approximation
     0 <= x <  35610; y_0      =       76.1782 +    -0.0001x; least squares approximation
     0 <= x <  35610; y_0      =       65.0242 +    -0.0001x; least squares approximation
     0 <= x <  35610; y_0      =       72.6798 +    -0.0001x; least squares approximation
```

## calculate_all.py Usage

### Requirements
    * Python 3.7

### Sample Execution
If executed with an invalid file name or without command line arguments, like so 
```
./least_squares.py
```
The following error message will display
```
Please provide a valid input file
```
If provided a path to a valid input file, like sensors2018.12.26-no-labels.txt as provided in the assignment prompt, like so
```
./calculate_all.py sensors2018.12.26-no-labels.txt
```
The following success message should display
```
All calculations completed successfully
```
New output files will also be created, containing the calculations for each core.
They will be named output_core_n.txt where n is the number of the core, starting with core 0