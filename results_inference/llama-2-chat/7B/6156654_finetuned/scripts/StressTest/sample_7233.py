distance_sita_geeta_premise = 2
distance_sita_geeta_hypothesis = 3

# the hypothesis talks about the distance each twin sister ran, which is also mentioned in the premise
if distance_sita_geeta_hypothesis >= distance_sita_geeta_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis distance is less than the premise distance, it entails the premise
    label = "entailment"

print(label)
