banks_premise = 117
banks_hypothesis = 90

# the hypothesis refers to the number of banks on the problem list in the second quarter
if banks_premise!= banks_hypothesis:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
