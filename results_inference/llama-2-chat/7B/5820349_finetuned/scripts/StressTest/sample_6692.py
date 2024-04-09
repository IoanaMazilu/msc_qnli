distance_travelled_air_premise = 1800
distance_travelled_air_hypothesis = 7800
total_distance_premise = (distance_travelled_air_premise / 3) + (distance_travelled_air_premise / 5)
total_distance_hypothesis = (distance_travelled_air_hypothesis / 3) + (distance_travelled_air_hypothesis / 5)

# the hypothesis refers to the distance travelled by air mentioned in the premise
if distance_travelled_air_premise!= distance_travelled_air_hypothesis:
    # check if the distance travelled by air in the hypothesis contradicts the distance travelled by air reported in the premise
    label = "contradiction"
elif total_distance_premise!= total_distance_hypothesis:
    # check if the total distance travelled by air in the hypothesis contradicts the total distance travelled by air reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
