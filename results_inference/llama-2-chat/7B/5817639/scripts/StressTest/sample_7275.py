rate_premise = 100
rate_hypothesis = 400

# the hypothesis refers to a lower speed than the premise
if rate_hypothesis <= rate_premise:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed lower than 'rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
