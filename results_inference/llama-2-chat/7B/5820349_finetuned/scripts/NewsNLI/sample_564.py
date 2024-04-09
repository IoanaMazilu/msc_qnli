redeemed_miles_premise = 0.4
redeemed_miles_hypothesis = 0.4

# the hypothesis mentions the percentage of people who never redeem loyalty miles, which is also mentioned in the premise
if redeemed_miles_hypothesis!= redeemed_miles_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
