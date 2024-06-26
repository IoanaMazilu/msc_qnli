distance_bitung_premise = 156
distance_tobelo_premise = 164
distance_coast_hypothesis = 150

# the hypothesis mentions the earthquake's distance from the coast, which is not fully detailed in the premise
if distance_coast_hypothesis < distance_bitung_premise and distance_coast_hypothesis < distance_tobelo_premise:
    # check if the distance from the coast in the hypothesis is less than the distances mentioned in the premise
    label = "contradiction"
else:
    # if the distance from the coast in the hypothesis is not less than the distances mentioned in the premise, we can infer neutrality
    label = "neutral"

print(label)
