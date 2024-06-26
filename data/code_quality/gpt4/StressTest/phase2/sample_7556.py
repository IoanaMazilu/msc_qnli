cleaning_time_premise = 6
cleaning_time_hypothesis = 5

# the hypothesis refers to the same cleaning time mentioned in the premise
if cleaning_time_hypothesis == cleaning_time_premise:
    # check if the cleaning time in the hypothesis matches the cleaning time reported in the premise
    label = "entailment"
elif cleaning_time_hypothesis > cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time reported in the premise
    label = "contradiction"
else:
    # if the cleaning time in the hypothesis is less than the cleaning time in the premise, it does not contradict the premise, but it cannot be explicitly entailed from it either
    label = "neutral"

print(label)
