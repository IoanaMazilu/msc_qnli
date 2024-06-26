days_premise = 16
days_hypothesis = 76

# the hypothesis refers to the number of days Mary will take to complete a task alone, as mentioned in the premise
if days_hypothesis!= days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
