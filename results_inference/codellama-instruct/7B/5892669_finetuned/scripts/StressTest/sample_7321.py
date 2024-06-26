gym_visits_premise = 2
gym_visits_hypothesis = 2
weeks_premise = 6
weeks_hypothesis = 3

# the hypothesis refers to the number of gym visits and the duration mentioned in the premise
if gym_visits_hypothesis!= gym_visits_premise:
    # check if the number of gym visits in the hypothesis contradicts the number of gym visits reported in the premise
    label = "contradiction"
elif weeks_hypothesis >= weeks_premise:
    # check if the duration in the hypothesis contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration
    # any duration less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
