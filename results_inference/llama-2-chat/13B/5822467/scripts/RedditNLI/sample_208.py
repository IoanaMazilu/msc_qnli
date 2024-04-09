# define variables with representative names for the numerical entities in both inputs
home_ownership_premise = 1960s
home_ownership_hypothesis = 1965

# extract all quantities as valid numbers (integers or floats)
home_ownership_premise_as_float = float(home_ownership_premise)
home_ownership_hypothesis_as_float = float(home_ownership_hypothesis)

# compare the variables
if home_ownership_hypothesis_as_float!= home_ownership_premise_as_float:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif home_ownership_hypothesis_as_float < home_ownership_premise_as_float:
    # check if the hypothesis value is less than the premise value
    label = "entailment"
else:
    # the hypothesis value is greater than or equal to the premise value
    label = "neutral"

print(label)
