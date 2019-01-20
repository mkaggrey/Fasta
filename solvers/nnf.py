import numpy as np
import fasta as fast

def solve(S, X0, Y0, mu, options):
    Z0 = np.vstack((X0,Y0))
    xrows = range(X0.shape[0])
    yrows = range(X0.shape[0], Z0.shape[0])

    def f(x):
        return 0.5 * np.linalg.norm(np.matmul(x[xrows],x[yrows].T) - S)**2

    def A(x):
        return x

    def At(x):
        return x

    def fgrad(x):
        X = x[xrows,:]
        Y = x[yrows,:]

        diff = np.matmul(X,Y.T) - S
        dX = np.matmul(diff,Y)
        dY = np.matmul(diff.T,X)
        grad = np.vstack((dX,dY))

        return grad

    def g(x):
        return 0

    def prox(x,t):
        x_max = np.maximum(x[xrows,:]-t*mu,0)
        y_opt = np.minimum(np.maximum(x[yrows,:],0),1)
        return np.vstack((x_max,y_opt))

    fasta = fast.Fasta(A, At, f, fgrad, g, prox, Z0, options)

    return fasta.run()

