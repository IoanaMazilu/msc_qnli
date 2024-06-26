# Define variables with representative names for the numerical entities in both inputs
purses_faiza_premise = 8
purses_given_premise = 3
purses_faiza_hypothesis = 5
purses_given_hypothesis = 3

# Extract all quantities as valid numbers (integers or floats)
purses_faiza_premise = int(purses_faiza_premise)
purses_given_premise = int(purses_given_premise)
purses_faiza_hypothesis = int(purses_faiza_hypothesis)
purses_given_hypothesis = int(purses_given_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if purses_faiza_hypothesis <= purses_faiza_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
elif purses_given_hypothesis!= purses_given_premise:
    # Check if the number of purses given in the hypothesis contradicts the number of purses given in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
