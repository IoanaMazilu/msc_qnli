premise = "How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?"
hypothesis = "How much loss would Indu has suffered had she given it to Bindu for less than 2 years at 4% per annum simple interest?"

# extract the numerical entities from the premise and hypothesis
premise_years = 2
premise_interest = 4
hypothesis_years = 1
hypothesis_interest = 4

# compare the numerical entities
if premise_years > hypothesis_years:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif premise_interest > hypothesis_interest:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is consistent with the premise value
    label = "neutral"

print(label)
