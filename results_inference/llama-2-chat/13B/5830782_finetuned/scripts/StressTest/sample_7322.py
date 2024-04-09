gym_visits_premise = 2
gym_visits_hypothesis = 2
weeks_premise = 3
weeks_hypothesis = 1

# the hypothesis refers to the average gym visits and the time frame mentioned in the premise
if gym_visits_hypothesis!= gym_visits_premise:
    # check if the average gym visits in the hypothesis contradicts the average gym visits reported in the premise
    label = "contradiction"
elif weeks_hypothesis > weeks_premise:
    # check if the time frame in the hypothesis contradicts the time frame reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
