deal_value_premise = 5.1
deal_value_hypothesis = 5.1

# the hypothesis and premise mention the deal value for the acquisition of Costa Coffee by Coca-Cola
if deal_value_hypothesis!= deal_value_premise:
    # check if the deal value in the hypothesis contradicts the deal value in the premise
    label = "contradiction"
else:
    # if the deal values in the hypothesis and premise do not contradict each other, we can infer entailment
    label = "entailment"

print(label)