prize_premise = 152000000
prize_hypothesis = 152000000

# the hypothesis mentions the amount of the after-tax prize, which is also mentioned in the premise
if prize_hypothesis != prize_premise:
    # check if the amount in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
