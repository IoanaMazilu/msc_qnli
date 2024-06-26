weeks_premise = 6
weeks_hypothesis = 3
average_gym_visits = 2

# the hypothesis refers to Rikki's gym visits in a period of weeks, which are also mentioned in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the premise estimate of 'weeks_premise'
    label = "contradiction"
else:
    # the premise gives an estimate of less than 'weeks_premise' for the number of weeks
    # 'weeks_hypothesis' weeks is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
