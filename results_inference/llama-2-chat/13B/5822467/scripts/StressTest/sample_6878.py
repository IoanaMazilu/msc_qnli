amar_age_premise = 20
akbar_age_premise = 25
anthony_age_premise = 16

# define variables with representative names for the numerical entities in both inputs
total_ages_premise = amar_age_premise + akbar_age_premise + anthony_age_premise

# extract all quantities as valid numbers (integers or floats)
total_ages_hypothesis = 20 + 25 + 16

# compare the variables
if total_ages_hypothesis < total_ages_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif total_ages_hypothesis > total_ages_premise:
    # the hypothesis entails the premise
    label = "entailment"
else:
    # the premise gives a specific value, the hypothesis gives a range
    # no comparison can be made, the label is neutral
    label = "neutral"

print(label)
