distance_travelled_premise = 1800
distance_travelled_hypothesis = 7800
fraction_air_journey_premise = 3/5
fraction_air_journey_hypothesis = 3/5

# the hypothesis talks about the distance travelled by Rakesh, which is also mentioned in the premise
if distance_travelled_hypothesis!= distance_travelled_premise:
    # check if the distance travelled in the hypothesis contradicts the distance travelled reported in the premise
    label = "contradiction"
# the premise and hypothesis are not contradicting, but the hypothesis cannot be fully and explicitly entailed from the premise
elif fraction_air_journey_hypothesis!= fraction_air_journey_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
