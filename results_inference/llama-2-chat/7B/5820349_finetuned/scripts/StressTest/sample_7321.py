gym_visits_premise = 6
gym_visits_hypothesis = 3
gym_visits_per_week_premise = 2
gym_visits_per_week_hypothesis = 2

# the hypothesis refers to the number of weeks Rikki has gone to the gym, which is also mentioned in the premise
if gym_visits_hypothesis >= gym_visits_premise:
    # check if the number of weeks in the hypothesis contradicts the premise's estimate of less than 'gym_visits_premise' weeks
    label = "contradiction"
elif gym_visits_per_week_hypothesis!= gym_visits_per_week_premise:
    # check if the number of gym visits per week in the hypothesis contradicts the number of gym visits per week reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of weeks Rikki has gone to the gym
    # any number of weeks less than 'gym_visits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
