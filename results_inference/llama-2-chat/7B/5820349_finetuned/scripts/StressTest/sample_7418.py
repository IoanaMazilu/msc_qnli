years_future_premise = 18
years_future_hypothesis = 20

# the hypothesis refers to the same situation as the premise, but with a different number of years in the future
if years_future_hypothesis <= years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of years in the future, while the hypothesis refers to more years
    # the hypothesis cannot be explicitly entailed from the premise, but does not contradict it either
    label = "neutral"

print(label)
