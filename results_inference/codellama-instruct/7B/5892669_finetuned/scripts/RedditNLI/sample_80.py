deal_value_premise = 5.1
deal_value_hypothesis = 5.1

# the hypothesis and premise mention the value of the deal
if deal_value_hypothesis!= deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the deal value in the hypothesis does not contradict the deal value in the premise, we can infer entailment
    label = "entailment"

print(label)
