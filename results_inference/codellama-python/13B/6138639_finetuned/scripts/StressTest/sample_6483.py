distance_premise = 20
distance_hypothesis = 80
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between their homes and the speeds of Maxwell and Brad mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif maxwell_speed!= 4 or brad_speed!= 6:
    # check if the speeds of Maxwell and Brad in the hypothesis contradict the speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
