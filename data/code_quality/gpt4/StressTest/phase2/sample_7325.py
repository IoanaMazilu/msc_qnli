weeks_premise = 1
weeks_hypothesis = 5
gym_visits_premise = 3
gym_visits_hypothesis = 3

# the hypothesis refers to the same event presented in the premise, but after a different number of weeks
if gym_visits_hypothesis != gym_visits_premise:
    # check if the number of gym visits in the hypothesis contradicts the number of gym visits reported in the premise
    label = "contradiction"
elif weeks_hypothesis != weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
