# Questions and thoughts
    * Isn't the uncertainty estimate skewed as continuous epochs should correlate quite strong?  

    * Approach still seems quite expensive to compute, e. g. ~ 15mio. x 20 forwards for Imagenet-21k, just for pruning. It's certainly nice that this should

    * How does the exact bi-level optimization problem look like?

    * Approach already requires labled data

    * Isn't some kind of burn-in required

    * Out-of-distribution generalisation seems quite interesting. However, they go from
    21.98 (0%) -> 22.61 (30%) -> 21.85 (50%). The CI overlap a bit. How impressive is this result? 

# Critic

    * Algorithm not clear "Sample a Batch B ~ T"