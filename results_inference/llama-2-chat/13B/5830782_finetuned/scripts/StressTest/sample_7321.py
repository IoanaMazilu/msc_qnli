weeks_premise = 6
weeks_hypothesis = 3
average_gym_visits = 2

# the hypothesis refers to the number of weeks and average gym visits mentioned in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif average_gym_visits!= average_gym_visits:
    # check if the average gym visits in the hypothesis contradicts the average gym visits reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
