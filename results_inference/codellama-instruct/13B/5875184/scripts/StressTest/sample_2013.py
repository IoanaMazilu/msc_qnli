premise = "How much loss would Indu has suffered had she given it to Bindu for 2 years at 4% per annum simple interest?"
hypothesis = "How much loss would Indu has suffered had she given it to Bindu for less than 6 years at 4% per annum simple interest?"

# extract the numerical entities from the premise and hypothesis
premise_years = 2
premise_interest = 4
hypothesis_years = 6
hypothesis_interest = 4

# check if the hypothesis years are less than the premise years
if hypothesis_years < premise_years:
    # check if the hypothesis interest is less than the premise interest
    if hypothesis_interest < premise_interest:
        # the hypothesis is more favorable than the premise, so it entails the premise
        label = "entailment"
    else:
        # the hypothesis interest is not less than the premise interest, so it contradicts the premise
        label = "contradiction"
else:
    # the hypothesis years are not less than the premise years, so it is neutral
    label = "neutral"

print(label)
