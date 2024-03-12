# Questions and thoughts

    * Approach still seems quite expensive to compute, e. g. ~ 15mio. x 20 forwards and backwards for Imagenet-21k, just for pruning. It's certainly nice that it's a uone-time thing

    * What about class balance? Dynamic Uncertainty does not care about it

    * Isn't the uncertainty estimate skewed as continuous epochs should correlate quite strong? 

    * Sidequestion: Wouln't adversarial training also benefit from training on the ones with dynamic uncertainty i. e. these should be closest to the decision boundry?

    * Approach already requires labled data 

    * Isn't some kind of burn-in required

    * Out-of-distribution generalisation seems quite interesting. However, they go from
        21.98 (0%) -> 22.61 (30%) -> 21.85 (50%). The CI overlap a bit. How impressive is this result? 

# Critic

    * Algorithm not clear "Sample a Batch B ~ T"