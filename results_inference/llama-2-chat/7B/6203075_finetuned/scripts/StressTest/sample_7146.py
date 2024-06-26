number_premise = 4
number_hypothesis = 8

# the hypothesis refers to the number mentioned in the premise
if number_hypothesis!= number_premise:
    # check if the number in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
