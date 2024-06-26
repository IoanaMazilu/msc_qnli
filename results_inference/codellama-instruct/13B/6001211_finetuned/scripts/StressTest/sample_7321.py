weeks_premise = 6
weeks_hypothesis = 3
gym_times_premise = 2
gym_times_hypothesis = 2

# the hypothesis refers to the number of weeks and the average gym times per week mentioned in the premise
if weeks_hypothesis >= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif gym_times_hypothesis!= gym_times_premise:
    # check if the average gym times per week in the hypothesis contradicts the average gym times per week reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks
    # any number of weeks less than 'weeks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
