total_journey_premise = 1800
total_journey_hypothesis = 8800
air_distance_premise = 3/5 * total_journey_premise
air_distance_hypothesis = 3/5 * total_journey_hypothesis

# the hypothesis talks about the distance travelled by air, which is also referenced in the premise
if air_distance_hypothesis <= air_distance_premise:
    # check if the hypothesis value contradicts the estimate of 'air_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled by air
    # any distance travelled by air that is less than 'air_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
