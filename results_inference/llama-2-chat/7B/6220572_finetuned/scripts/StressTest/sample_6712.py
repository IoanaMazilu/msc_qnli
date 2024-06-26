balls_premise = 77
balls_hypothesis = 17

if balls_hypothesis >= balls_premise:
    label = "entailment"
elif balls_hypothesis > balls_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
