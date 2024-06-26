weeks_premise = 3
average_gym_visits_premise = 2
weeks_hypothesis = 1
average_gym_visits_hypothesis = 2

# the hypothesis refers to the same average gym visits per week as the premise
# but considers a shorter period of time
if average_gym_visits_premise != average_gym_visits_hypothesis:
    # check if the hypothesis contradicts the average gym visits per week from the premise
    label = "contradiction"
elif weeks_hypothesis > weeks_premise:
    # check if the hypothesis considers a period longer than in the premise
    label = "contradiction"
else:
    # if the average visits per week is consistent with the premise for the period of time considered in the hypothesis
    # we can infer entailment
    label = "entailment"

print(label)
