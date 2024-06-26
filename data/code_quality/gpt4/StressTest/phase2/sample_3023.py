tip_rate_john_premise = 15
tip_rate_john_hypothesis = 55

# the hypothesis refers to the tip rate paid by John, mentioned also in the premise
if tip_rate_john_hypothesis != tip_rate_john_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis are consistent regarding Jane's tip payment
    # if the tip rate for John in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)
