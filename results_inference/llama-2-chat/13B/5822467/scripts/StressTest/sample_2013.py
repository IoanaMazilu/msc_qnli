interest_premise = 4
years_premise = 2

# define variables for the numerical entities in the premise
loss_premise = interest_premise * years_premise

# define variables for the numerical entities in the hypothesis
loss_hypothesis = hypothesis_less_than_6_years = (interest_premise * years_hypothesis)

# compare the variables
if loss_hypothesis <= loss_premise:
    # the hypothesis value is consistent with the premise value
    label = "neutral"
elif years_hypothesis < 6:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value entails the premise value
    label = "entailment"

print(label)
