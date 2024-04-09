speed_to_beach_premise = 80
speed_to_beach_hypothesis = 60
speed_from_beach_premise = 70
speed_from_beach_hypothesis = 70

# the hypothesis refers to the speed Carl drove to the beach and from the beach, mentioned in the premise
if speed_to_beach_premise!= speed_to_beach_hypothesis:
    # check if the speed to the beach in the hypothesis contradicts the speed to the beach reported in the premise
    label = "contradiction"
elif speed_from_beach_premise!= speed_from_beach_hypothesis:
    # check if the speed from the beach in the hypothesis contradicts the speed from the beach reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
