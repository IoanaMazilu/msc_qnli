toy_rate_premise = 375
toy_rate_hypothesis = 675

# the hypothesis talks about the rate at which Venkat purchased toys, referenced also in the premise
if toy_rate_hypothesis <= toy_rate_premise:
    # check if the hypothesis value contradicts the estimate of 375 per dozen
    label = "contradiction"
else:
    # the premise gives only an estimate for the rate at which Venkat purchased toys
    # any rate greater than 375 per dozen is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
