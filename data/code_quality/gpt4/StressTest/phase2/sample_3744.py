paper_reams_purchased_premise = 120
paper_reams_purchased_hypothesis = 220
price_per_ream = 80

# the hypothesis refers to the number of reams of paper purchased mentioned in the premise
if paper_reams_purchased_premise >= paper_reams_purchased_hypothesis:
    # check if the hypothesis statement contradicts the number of paper reams purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
