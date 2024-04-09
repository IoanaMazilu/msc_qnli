travel_distance_premise = 1800
travel_distance_hypothesis = 8800

# the hypothesis refers to the distance travelled by air, which is also mentioned in the premise
if travel_distance_hypothesis <= travel_distance_premise:
    # check if the estimate of 'travel_distance_hypothesis' contradicts the distance travelled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
