# predictive algorithm of latent states based on viterbi path 
# given a set of HMM model parameters
predictStates <- function(x, m, mu, sigma, gamma, delta=NULL, ...) {
        # this function is based on a gaussian HMM viterbi algorithm
        # x is a matrix of observations of size N * X
        # m is a scalar with the number of states
        # mu is a vector with the state conditional means (1 * M)
        # sigma is a vector with the state conditional stdev (1 * M)
        # gamma is a square matrix of transition probabilities of size (M * M)
        # delta is a vector with the initial state probabilities (1 * M)
        
        if (!require(dplyr)) {
                install.packages("dplyr")
        }
        library(dplyr)
        
        if (is.null(delta)) {
                delta = solve(t(diag(m) - gamma + 1), rep(1, m))
        }
        n = nrow(x) # number of observations
        
        # compute likelihood
        gaussProbs = suppressWarnings(gaussProb(x, m, mu, sigma))

        # compute posterior
        xi = matrix(0, n, m) # initialize matrix
        xi[1,] = delta * gaussProbs[1, ] # compute first observation
        xi[1,] = gaussProbs[1, ] # compute first observation
        # for the rest observations
        for (i in 2:n) {
                foo = apply(xi[i - 1, ] * gamma, 2, max) * gaussProbs[i, ]
                xi[i, ] = foo / sum(foo)
                if (sum(xi[i, ]) < .99) {
                  cat("\nError: probs don't add to 1 at step", t, " --\n ")
                  print(foo)
                  stop("bad posterior probabilites")
                }

        }

        # compute backward state
        iv = numeric(n)
        iv[n] = which.max(xi[n-1, ])
        for (i in (n - 1):1) {
                iv[i] = which.max(gamma[, iv[i + 1]] * xi[i, ])
        }
        return(posterior = iv)
}

# help function
gaussProb <- function(x, m, mu, sigma) {
        # returns a matrix of P(Ci|X) of size (N * M)
        
        # smooth data to get rid of outliers
        x = x %>% sapply(smooth)
        
        # for i in m states
        gaussProbX1 = sapply(1:m, function(i) {
                dnorm(x[, 1], mu[i, 1], sigma[i, 1]) 
        })
        gaussProbX2 = sapply(1:m, function(i) {
                dnorm(x[, 2], mu[i, 2], sigma[i, 2]) 
        })
        
        # make sure there are no NA's probabilities
        gaussProbX1[is.na(gaussProbX1) | gaussProbX1 == 0.000000e+00] = 1e-30
        gaussProbX2[is.na(gaussProbX2) | gaussProbX1 == 0.000000e+00] = 1e-30
        
        # for time t in n
        n = nrow(x)
        gaussProbX = matrix(0, ncol = m, nrow = n)
        for (t in 1:n) {
          foo = gaussProbX1[t, ] * gaussProbX2[t, ]
          if (sum(foo) == 0) {
            cat("\nError: gaussian inner product sums to 0 at step", t, " --\n ")
            print(foo)
            stop("bad gaussians")
          }
          gaussProbX[t, ] = foo / sum(foo)
          if (sum(gaussProbX[t, ]) < .99) {
            cat("\nError: probs don't add to 1 at step", t, " --\n ")
            print(sum(gaussProbX[t, ]))
            stop("bad probabilities")
          }
        }
        
        return(gaussProbX)
}

