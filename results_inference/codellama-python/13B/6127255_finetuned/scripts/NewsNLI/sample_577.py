prize_amount_premise = 10000000
prize_amount_hypothesis = 10000000

# the hypothesis mentions the amount of the prize, which is also mentioned in the premise
if prize_amount_hypothesis!= prize_amount_premise:
    # check if the prize amount in the hypothesis contradicts the prize amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis prize amount does not contradict the premise prize amount, we can infer entailment
    label = "entailment"

print(label)
