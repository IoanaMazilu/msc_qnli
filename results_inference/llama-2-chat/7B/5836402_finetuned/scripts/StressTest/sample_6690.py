air_travel_km_premise = 1800
air_travel_km_hypothesis = 8800
total_journey_km_premise = 3/5 * air_travel_km_premise
total_journey_km_hypothesis = 3/5 * air_travel_km_hypothesis

# the hypothesis refers to the total journey distance, which is also mentioned in the premise
if air_travel_km_premise <= air_travel_km_hypothesis:
    # check if the estimate of 'air_travel_km_hypothesis' contradicts the total journey distance in the premise
    label = "contradiction"
elif total_journey_km_hypothesis!= total_journey_km_premise:
    # check if the total journey distance in the hypothesis contradicts the total journey distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
