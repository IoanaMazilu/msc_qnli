return_on_investment_premise = 2
return_on_investment_hypothesis = 3

# the hypothesis talks about the return on investment at the end of 'n' years, which is also mentioned in the premise
if return_on_investment_hypothesis <= return_on_investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif return_on_investment_hypothesis > return_on_investment_premise:
    # the premise gives exactly how much Sandy got back
    # any return on investment less than 'return_on_investment_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
