percentage_premise = 4
percentage_hypothesis = 6

# the hypothesis refers to the percentage of the amount given back by Dana, referenced also in the premise
if percentage_hypothesis >= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
