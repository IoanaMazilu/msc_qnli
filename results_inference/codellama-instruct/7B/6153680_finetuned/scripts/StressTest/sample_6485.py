distance_premise = 20
distance_hypothesis = 20
walking_speed_premise = 4
walking_speed_hypothesis = 4
running_speed_premise = 6
running_speed_hypothesis = 6

# the hypothesis refers to the same situation as the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif walking_speed_hypothesis!= walking_speed_premise or running_speed_hypothesis!= running_speed_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values and premise values do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
