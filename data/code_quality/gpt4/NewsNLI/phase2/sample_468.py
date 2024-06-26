distance_km_premise = 500
distance_miles_premise = 310
distance_miles_hypothesis = 310

# the hypothesis mentions the distance between the crash site and Algiers, which is also mentioned in the premise
if distance_miles_hypothesis != distance_miles_premise:
    # check if the distance in miles from the hypothesis contradicts the distance in miles reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
