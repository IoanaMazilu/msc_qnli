visits_gym_premise = 3
visits_gym_hypothesis = 6

# the hypothesis refers to the number of visits to the gym mentioned in the premise
if visits_gym_hypothesis <= visits_gym_premise:
    # check if the estimate of 'visits_gym_hypothesis' contradicts the number of visits to the gym in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
