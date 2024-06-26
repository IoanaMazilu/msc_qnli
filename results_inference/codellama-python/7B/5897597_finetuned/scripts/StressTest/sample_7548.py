decrease_percentage_premise = 30
decrease_percentage_hypothesis = 80

# the hypothesis refers to the decrease percentage of John's Bank's saving amount due to loan payment, mentioned in the premise
if decrease_percentage_hypothesis < decrease_percentage_premise:
    # check if the decrease percentage in the hypothesis contradicts the decrease percentage in the premise
    label = "contradiction"
else:
    # if the decrease percentage in the hypothesis does not contradict the decrease percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
