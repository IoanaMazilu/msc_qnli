gym_premise = 2
gym_hypothesis = 1

# the hypothesis refers to the number of weeks and the increase in gym visits
if gym_hypothesis <= gym_premise:
    # check if the hypothesis value contradicts the number of weeks in the premise
    label = "contradiction"
elif gym_hypothesis == gym_premise:
    # check if the hypothesis value is consistent with the number of weeks in the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks greater than 'gym_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
