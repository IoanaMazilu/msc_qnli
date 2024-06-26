weeks_premise = 1
weeks_hypothesis = 5
average_gym_visits_premise = 3
average_gym_visits_hypothesis = 3

# the hypothesis refers to the number of weeks and average gym visits mentioned in the premise
if weeks_hypothesis!= weeks_premise:
    # check if the number of weeks in the hypothesis contradicts the number of weeks reported in the premise
    label = "contradiction"
elif average_gym_visits_hypothesis!= average_gym_visits_premise:
    # check if the average gym visits in the hypothesis contradicts the average gym visits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
