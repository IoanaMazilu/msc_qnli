distance_premise = 40
distance_hypothesis = 50
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes and the walking/running speeds of Maxwell and Brad mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_premise != maxwell_speed_hypothesis or brad_speed_premise != brad_speed_hypothesis:
    # check if the speeds of Maxwell and Brad in the hypothesis contradict the speeds mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
