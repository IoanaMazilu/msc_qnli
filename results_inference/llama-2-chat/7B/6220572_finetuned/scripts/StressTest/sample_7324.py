average_gym_visits_premise = 2
average_gym_visits_hypothesis = 1

# the hypothesis refers to the number of weeks until the average number of gym visits increases
if average_gym_visits_hypothesis >= average_gym_visits_premise:
    # check if the hypothesis estimate contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks greater than 'average_gym_visits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
