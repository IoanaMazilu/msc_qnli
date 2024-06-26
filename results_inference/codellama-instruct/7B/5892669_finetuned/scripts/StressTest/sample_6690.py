travelled_distance_premise = 1800
travelled_distance_hypothesis = 8800

# the hypothesis refers to the distance travelled by Rakesh mentioned in the premise
if travelled_distance_premise >= travelled_distance_hypothesis:
    # check if the estimate of 'travelled_distance_hypothesis' contradicts the distance travelled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
