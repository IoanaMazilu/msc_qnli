deal_value_premise = 7.2
deal_value_hypothesis = 7.15

# the hypothesis and premise mention the deal value between Nestle and Starbucks
if deal_value_hypothesis > deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
elif deal_value_hypothesis < deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the deal value in the hypothesis does not contradict the deal value in the premise, we can infer entailment
    label = "entailment"

print(label)
