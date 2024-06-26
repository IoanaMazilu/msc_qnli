air_travel_distance_premise = 1800
air_travel_distance_hypothesis = 7800
total_journey_premise = 3/5
total_journey_hypothesis = 3/5

# the hypothesis refers to the distance travelled by air in the premise
if air_travel_distance_hypothesis!= air_travel_distance_premise:
    # check if the distance travelled by air in the hypothesis contradicts the distance travelled by air in the premise
    label = "contradiction"
elif total_journey_hypothesis!= total_journey_premise:
    # check if the total journey in the hypothesis contradicts the total journey reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
