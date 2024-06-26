future_gym_visits_premise = 3
future_gym_visits_hypothesis = 3

# the hypothesis talks about the future number of gym visits, which is also referenced in the premise
if future_gym_visits_hypothesis!= future_gym_visits_premise:
    # check if the future number of gym visits in the hypothesis contradicts the future number of gym visits in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
