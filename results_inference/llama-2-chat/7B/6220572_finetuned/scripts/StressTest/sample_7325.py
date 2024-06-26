increase_week_premise = 1
increase_week_hypothesis = 5

# the hypothesis refers to the increase in the number of times Rikki goes to the gym per week, also mentioned in the premise
if increase_week_hypothesis <= increase_week_premise:
    # check if the hypothesis value contradicts the increase in number of times per week in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks until the increase in Rikki's gym visits
    # any number of weeks greater than 'increase_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
