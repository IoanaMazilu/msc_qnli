offer_premise = 30
offer_hypothesis = 80

# the hypothesis talks about the discount offered for a shirt, similar to the premise
if offer_hypothesis != offer_premise:
    # check if the discount rate in the hypothesis contradicts the discount rate given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
