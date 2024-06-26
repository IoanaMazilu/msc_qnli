cleaning_time_premise = 6
cleaning_time_hypothesis = 6

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis statement contradicts the premise one
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
