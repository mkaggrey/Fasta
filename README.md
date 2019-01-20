# Fasta
## How to use FASTA?
Before using FASTA, please see:

> [A Field Guide to Forward-Backward Splitting with a FASTA Implementation](https://arxiv.org/abs/1411.3406) <br>

Users can also reference [main FASTA webpage](https://www.cs.umd.edu/~tomg/projects/fasta/) for a more detailed
overview of FASTA, and of forward-backward optimization methods in general.  

## What can FASTA solve?

Let *A* to be a linear operator, *f* some differentiable function, and *g* some simple function (not neccesarily smooth). 
FASTA targets problems of the form:

_minimize f(Ax)+g(x)_

Problems of this form including sparse least-squares (basis-pursuit), lasso, total-variation denoising, matrix completion, 
and many more. The FASTA implementation is incredibly flexible; users can solve almost anything by providing their 
own "f," g," and "A." Additional "out-of-the-box" solvers coming shortly.  

For a more extensive list of problems, and their mathematical formulations, see the
[main FASTA webpage](https://www.cs.umd.edu/~tomg/projects/fasta/).

Note: This is an updated version of an older repository that no longer exists. 
