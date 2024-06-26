air_distance_premise = 1800
air_distance_hypothesis = 8800

# the hypothesis refers to the distance travelled by air mentioned in the premise
if air_distance_premise >= air_distance_hypothesis:
    # check if the estimate of 'air_distance_hypothesis' contradicts the distance travelled by air in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
