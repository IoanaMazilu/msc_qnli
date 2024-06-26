# Define variables with representative names for the numerical entities in both inputs
matches_premise = 23
relegation_premise = "Lens"
impressions_hypothesis = "Varane"

# Extract all quantities as valid numbers (integers or floats)
matches_premise = int(matches_premise)
relegation_premise = str(relegation_premise)
impressions_hypothesis = str(impressions_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if matches_premise!= 0:
    # Check if the number of matches played by Varane contradicts the number of matches played in the premise
    label = "contradiction"
elif relegation_premise!= "Ligue 1":
    # Check if the relegation status of Lens contradicts the relegation status mentioned in the premise
    label = "contradiction"
elif impressions_hypothesis!= "Varane":
    # Check if the name of the player mentioned in the hypothesis contradicts the name of the player mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
