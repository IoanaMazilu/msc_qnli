air_distance_premise = 1800
air_distance_hypothesis = 7800

# the hypothesis talks about the distance travelled by air, which is also referred to in the premise
if air_distance_hypothesis >= air_distance_premise * 3 / 5:
    # check if the hypothesis value contradicts the estimate of 'air_distance_premise' multiplied by 3/5
    label = "contradiction"
else:
    # the premise gives an estimate for the distance travelled by air, which can be fully entailed by the hypothesis
    label = "entailment"

print(label)
