cleaning_time_premise = 6
cleaning_time_hypothesis = 1

# the hypothesis refers to the time Jim takes to clean the entire house, as mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the cleaning time in the premise
    label = "contradiction"
elif cleaning_time_hypothesis < cleaning_time_premise:
    # check if the hypothesis value is less than the cleaning time in the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the cleaning time in the premise, we can infer entailment
    label = "entailment"

print(label)
