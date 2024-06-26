distance_run_by_sita_and_geeta_premise = 10
distance_run_by_sita_and_geeta_hypothesis = 20

# The hypothesis talks about the distance run by Sita and Geeta, referenced also in the premise
if distance_run_by_sita_and_geeta_hypothesis < distance_run_by_sita_and_geeta_premise:
    # If the distance given in the hypothesis is less than the distance mentioned in the premise, that's a contradiction
    label = "contradiction"
elif distance_run_by_sita_and_geeta_hypothesis == distance_run_by_sita_and_geeta_premise:
    # If the distance given in the hypothesis equals the distance mentioned in the premise, that's an entailment
    label = "entailment"
else:
    # If the distance given in the hypothesis is more than the distance mentioned in the premise, we can't directly infer from the premise, thus it's neutral
    label = "neutral"

print(label)
