chiefs_premise = 5
chiefs_hypothesis = 1

# the hypothesis refers to the number of Joint Chiefs of Staff at a meeting, mentioned in the premise
if chiefs_hypothesis!= chiefs_premise:
    # check if the number of chiefs in the hypothesis contradicts the number of chiefs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
