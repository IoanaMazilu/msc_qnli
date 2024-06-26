# Define variables for the numerical entities in the premise and hypothesis
premise_qualifying_position = 9
premise_relegation_places = 10
hypothesis_relegation_places = 10

# Extract all quantities as valid numbers
premise_qualifying_position = float(premise_qualifying_position)
premise_relegation_places = float(premise_relegation_places)
hypothesis_relegation_places = float(hypothesis_relegation_places)

# Check if the hypothesis contradicts the premise
if hypothesis_relegation_places!= premise_relegation_places:
    # The hypothesis mentions a different number of relegation places than the premise, so we can infer contradiction
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise values, we can infer neutral
    label = "neutral"

print(label)
