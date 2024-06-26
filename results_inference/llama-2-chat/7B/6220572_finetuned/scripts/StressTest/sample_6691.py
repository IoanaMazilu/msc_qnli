distance_air_premise = 8800
distance_air_hypothesis = 1800
total_distance_premise = 3/5 * distance_air_premise
total_distance_hypothesis = 3/5 * distance_air_hypothesis

# the hypothesis talks about the distance Rakesh travelled by air, also referenced in the premise
if distance_air_hypothesis >= distance_air_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_air_premise'
    label = "contradiction"
elif total_distance_hypothesis!= total_distance_premise:
    # check if the total distance in the hypothesis contradicts the total distance reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled by air
    # any distance less than 'distance_air_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
