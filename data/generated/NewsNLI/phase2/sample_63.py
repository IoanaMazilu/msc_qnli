# Premise: Quezada has chosen a cash payment of his lottery prize that will amount to approximately $152 million after taxes.
# Hypothesis: The payment was taken from his after-tax prize of about $152 million.
# Golden Label: entailment

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

