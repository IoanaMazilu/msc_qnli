# Define variables with representative names for the numerical entities in both inputs
passengers_premise = 32.3
passengers_hypothesis = 32.3
airport_premise = "Kennedy Airport"
airport_hypothesis = "Kennedy Airport"
year_premise = 1979
year_hypothesis = 1979

# Extract all quantities as valid numbers (integers or floats)
passengers_premise = float(passengers_premise)
passengers_hypothesis = float(passengers_hypothesis)
airport_premise = str(airport_premise)
airport_hypothesis = str(airport_hypothesis)
year_premise = int(year_premise)
year_hypothesis = int(year_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if passengers_premise <= passengers_hypothesis:
    # Check if the estimate of 'passengers_hypothesis' contradicts the number of passengers reported in the premise
    label = "contradiction"
elif airport_premise!= airport_hypothesis:
    # Check if the airport mentioned in the hypothesis contradicts the airport mentioned in the premise
    label = "contradiction"
elif year_premise!= year_hypothesis:
    # Check if the year mentioned in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
