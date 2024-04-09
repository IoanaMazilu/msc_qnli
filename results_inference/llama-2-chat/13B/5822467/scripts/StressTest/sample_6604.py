original_investment = 100
n_years = 5

# define variables with representative names for the numerical entities in both inputs
sandy_got_back_premise = original_investment * (1 - (n_years / 100))
sandy_got_back_hypothesis = 2 * original_investment

# extract all quantities as valid numbers (integers or floats)
sandy_got_back_premise = float(sandy_got_back_premise)
sandy_got_back_hypothesis = float(sandy_got_back_hypothesis)

# perform calculations if necessary
if sandy_got_back_hypothesis > sandy_got_back_premise:
    # check if the hypothesis value contradicts the premise estimate
    label = "contradiction"
elif sandy_got_back_hypothesis == sandy_got_back_premise:
    # check if the hypothesis value is consistent with the premise estimate
    label = "neutral"
else:
    # check if the hypothesis value entails the premise estimate
    label = "entailment"

print(label)
