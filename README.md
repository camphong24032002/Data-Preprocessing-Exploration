## **Data Mining - Data Preprocessing and Data Exploration**
Simple preprocessing implementation without library.
### **Features**
There are some basic data preprocessing tasks:
* List missing values
* Handle missing values
* Remove samples
* Normalize the values
* Performing expression on two attributes
### **How to use**
We use csv file to read and write. Each task above is split into corresponding file. We need to execute these file with terminal and use argument parameters to control.
## **List missing values**

This task provides:

* The number of missing attributes
* The missing attribute with its number of samples
* The number of missing samples

### **The missing attribute**
In order to run, we need to use:
```bash
list-missing.py <input-file>
```
Arguments:
* `<input-file>`: the input file path

### **The missing samples**

In order to run, we need to use:
```bash
count-missing.py <input-file>
```
Arguments:
* `<input-file>`: the input file path

## **Handle missing values**

In this task, we can impute the missing value using different methods on specific attributes:

* Mean: Fill with the mean of value (for numeric)
* Median: Fill with the median of value (for numeric)
* Mode: Fill with the most frequent value

In order to run, we need to use:
```bash
impute.py <input-file> --method=<method> --columns <column 1> ... <column N> --out=<output-file>
```
Arguments:
* `<input-file>`: the input file path
* `<method>`: the filling method (`mean`, `median`, `mode`)
* `<column 1> ... <column N>`: the columns we need to impute
* `<output-file>`: the output file path

## **Remove samples**

In this task, we can remove duplicated and missing values.

### **Duplicated samples**
In this feature, we can remove duplicates.

In order to run, we need to use:
```bash
drop-duplicates.py <input-file> --out=<output-file>
```
Arguments:
* `<input-file>`: the input file path
* `<output-file>`: the output file path

### **Missing value**
In this feature, we can drop the values whose missing rate is more than threshold. For instance, we will drop the value whose missing rate is more than 0.5.

In order to run, we need to use:
```bash
drop-threshold.py <input-file> --axis=<axis> --threshold=0.5 --out=<output-file>
```
Arguments:
* `<input-file>`: the input file path
* `<axis`: the axis we want to process (`sample`, `attribute`)
* `<output-file>`: the output file path


## **Normalize the values**

This task allows you to normalize the numeric value using different method on specific attributes

* Min-Max: Normalize the values to [0, 1] using the formula
$$x'=\frac{x-min}{max-min}$$
* Z-score: Normalize the values based on mean and standard deviation using the formula
$$x'=\frac{x-\mu}{\sigma}$$
 
In order to run, we need to use:
```bash
normalize.py <input-file> --method=<method> --columns <column 1> ... <column N> --out=<output-file>
```
Arguments:
* `<input-file>`: the input file path
* `<method>`: the normalizing method (`min-max`, `z-score`)
* `<column 1> ... <column N>`: the columns we need to normalize
* `<output-file>`: the output file path


## **Performing expression on two attributes**

In this task, we can perform expression on two numeric attributes:

* Addition: Plus two attributes
* Subtraction: Subtract two attributes
* Multiplication: Multiplicate two attributes
* Division: Divide the first attribute by the second attribute
 
In order to run, we need to use:
```bash
normalize.py <input-file> --expression=<expression> --columns <column 1> <column 2> --out=<output-file>
```
Arguments:
* `<input-file>`: the input file path
* `<expression>`: the expression we need to perform
* `<column 1> <column 2>`: the columns we need to normalize
* `<output-file>`: the output file path

## **Summary**
There are 7 files corresponding to its feature:
* `list-missing.py`
* `count-missing.py`
* `impute.py`
* `drop-duplicates.py`
* `drop-threshold.py`
* `normalize.py`
* `expression.py`

In order to handle these files, we use `File.py` to deal with csv file.

We build `Data.py` as the DataFrame which contains a list of samples and `Sample.py` as the sample. To deal with mathematic functions, we use `Utils.py` to process all of them.