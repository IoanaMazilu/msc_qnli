week_premise = 2
week_hypothesis = 1
average_gym_visits_premise = 3
average_gym_visits_hypothesis = 3

# the hypothesis refers to the number of weeks and average gym visits mentioned in the premise
if week_hypothesis >= week_premise:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'week_premise'
    label = "contradiction"
elif average_gym_visits_hypothesis!= average_gym_visits_premise:
    # check if the average gym visits in the hypothesis contradicts the average gym visits reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
