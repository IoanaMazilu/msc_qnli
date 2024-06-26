deal_value_premise = 5.1
deal_value_hypothesis = 5.1

# the hypothesis and premise mention the deal value for Costa Coffee
if deal_value_premise!= deal_value_hypothesis:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
