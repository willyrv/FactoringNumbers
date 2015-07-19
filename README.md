# FactoringNumbers
Python implementations of Fermat's factorization method and some improvements

Here I implement the Fermat's factorization method in its more naive way.
Then I add some improvements in order to speed up the algorithm.

I take as input a file called *input.txt* containing one number per line. The
output is a file called *output.txt* which has two factors (separated by one
  semicolom) by line. Each line of the *output.txt* file contains two factors
of the number in the corresponding line in the input file. If the number **n**
in the input file is prime, then the corresponding line in the output file will
be **(n; 1)**.

In the naive implementation, if numbers are too long, the **sqrt** method will give an error.
Moreover, if numbers are too big, it may be very slow.

For use it, just type in a terminal *./naiveffm.py*.
