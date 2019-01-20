import nnf
import numpy as np
import fasta as fast
import matplotlib.pyplot as plt

M = 800
N = 200
K = 10
mu = 1

X = np.random.rand(M,K)
Y = np.random.rand(N,K)

X[X < .75] = 0

S = np.matmul(X,Y.T) + np.random.rand(M,N)*.1

X0 = np.zeros((M,K))
Y0 = np.random.rand(N,K)

Z0 = np.vstack((X0,Y0))
xrows = range(X0.shape[0])
yrows = range(X0.shape[0], Z0.shape[0])




opts1 = fast.Options(recordObjective=True, verbose=True, stopRule=fast.Options.ITERATIONS)
outs1 = nnf.solve(S, X0, Y0, mu, opts1)

opts2 = fast.Options(adaptive=True, recordObjective=True, stopRule=fast.Options.ITERATIONS)
outs2 = nnf.solve(S, X0, Y0, mu, opts2)

opts3 = fast.Options(acceleration=True, recordObjective=True, stopRule=fast.Options.ITERATIONS)
outs3 = nnf.solve(S, X0, Y0, mu, opts3)


plt.figure(figsize=(20,15))

FBS_0, = plt.semilogy(outs1.residuals[:250], color='red',label="FBS")
FBS_1, = plt.semilogy(outs2.residuals[:250], color='green',label="FBS+Adaptive")
FBS_2, = plt.semilogy(outs3.residuals[:250], color='blue',label="FBS+Accelerate")

plt.legend(handles=[FBS_0,FBS_1, FBS_2])

plt.title("FASTA Residuals (Nonnegative Matrix Factorization)")
plt.xlabel("Iteration")
plt.ylabel("Residual")

plt.savefig("nnf_run.png", bbox_inches='tight')
