distance_walked_premise = 7
distance_walked_hypothesis = 3
time_walked = 1.25 # 1 hour and 15 minutes is 1.25 hours

# the hypothesis refers to the distance walked by Jack, which is also mentioned in the premise
if distance_walked_hypothesis!= distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the distance walked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
