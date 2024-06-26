increase_week_premise = 1
increase_week_hypothesis = 5

# the hypothesis refers to the number of weeks after which the average number of times Rikki goes to the gym increases, also mentioned in the premise
if increase_week_hypothesis <= increase_week_premise:
    # check if the hypothesis value contradicts the estimate of 'increase_week_premise'
    label = "contradiction"
elif increase_week_hypothesis > increase_week_premise:
    # check if the hypothesis value is greater than the premise value, which is not contradictory
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
