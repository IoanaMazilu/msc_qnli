toy_rate_premise = 275
toy_rate_hypothesis = 375

# the hypothesis talks about the rate of toys purchased by Venkat, referenced also in the premise
if toy_rate_hypothesis <= toy_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'toy_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate of toys
    # any rate greater than 'toy_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
