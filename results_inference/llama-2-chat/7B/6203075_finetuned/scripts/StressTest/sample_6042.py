distance_premise = 40
distance_hypothesis = 10
speed_maxwell_premise = 4
speed_maxwell_hypothesis = 4
speed_brad_premise = 6
speed_brad_hypothesis = 6

# the hypothesis refers to the distance between their homes and the speeds of Maxwell and Brad, both mentioned in the premise
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif speed_maxwell_premise!= speed_maxwell_hypothesis or speed_brad_premise!= speed_brad_hypothesis:
    # check if the speeds of Maxwell and Brad in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
