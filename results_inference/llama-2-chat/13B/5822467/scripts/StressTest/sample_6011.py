# define variables with representative names for the numerical entities in both inputs
bet_distance_premise = 4
bet_distance_hypothesis = 6
start_time_premise = 4

# extract all quantities as valid numbers (integers or floats)
if bet_distance_hypothesis > bet_distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif bet_distance_hypothesis == bet_distance_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # check if the premise value can be explicitly entailed from the hypothesis value
    label = "entailment"

print(label)
