gym_visits_premise = 2
gym_visits_hypothesis = 2
weeks_premise = 3
weeks_hypothesis = 1

# the hypothesis refers to the number of gym visits and the duration mentioned in the premise
if gym_visits_premise!= gym_visits_hypothesis:
    # check if the number of gym visits in the hypothesis contradicts the number of gym visits reported in the premise
    label = "contradiction"
elif weeks_premise < weeks_hypothesis:
    # check if the duration in the hypothesis contradicts the duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
