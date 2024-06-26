interest_rate_premise = 8
interest_rate_hypothesis = 7

# the hypothesis mentions a rate of interest greater than the rate mentioned in the premise
if interest_rate_hypothesis <= interest_rate_premise:
    # check if the hypothesis value contradicts the rate of interest in the premise
    label = "contradiction"
else:
    # the premise gives the rate of interest, but the hypothesis gives a more general statement
    # any rate of interest greater than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
