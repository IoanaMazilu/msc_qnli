distance_walked_premise = 7
distance_walked_hypothesis = 3
time_walked = 1.25 # 1 hour and 15 minutes converted to hours

# the hypothesis refers to the distance walked by Jack, mentioned also in the premise
if distance_walked_hypothesis!= distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the distance walked reported in the premise
    label = "contradiction"
else:
    # if the distance walked in the hypothesis does not contradict the distance walked in the premise, we can infer entailment
    label = "entailment"

print(label)
