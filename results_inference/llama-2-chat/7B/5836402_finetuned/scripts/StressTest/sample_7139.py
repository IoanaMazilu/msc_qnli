percentage_decrease_premise = 10
percentage_decrease_hypothesis = 40

# the hypothesis refers to the percentage decrease in David's Bank's saving amount, which is also mentioned in the premise
if percentage_decrease_hypothesis!= percentage_decrease_premise:
    # check if the percentage decrease in the hypothesis contradicts the percentage decrease in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
