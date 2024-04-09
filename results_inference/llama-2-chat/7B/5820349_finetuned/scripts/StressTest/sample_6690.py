distance_travelled_premise = 1800
distance_travelled_hypothesis = 8800

# the hypothesis refers to the distance travelled by air mentioned in the premise
if distance_travelled_hypothesis < distance_travelled_premise:
    # check if the estimate of 'distance_travelled_hypothesis' contradicts the distance travelled in the premise
    label = "contradiction"
elif distance_travelled_premise!= distance_travelled_hypothesis:
    # check if the distance travelled in the hypothesis contradicts the distance travelled reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
