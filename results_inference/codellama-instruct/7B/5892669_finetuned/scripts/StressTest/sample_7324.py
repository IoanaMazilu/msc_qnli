weeks_premise = 2
weeks_hypothesis = 1
average_gym_premise = 3
average_gym_hypothesis = 3

# the hypothesis refers to the number of weeks and the average number of gym visits mentioned in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif average_gym_hypothesis!= average_gym_premise:
    # check if the average number of gym visits in the hypothesis contradicts the number of gym visits reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
