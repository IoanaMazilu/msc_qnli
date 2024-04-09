cleaning_time_premise = 3
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
