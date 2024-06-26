money_mary_premise = 3803
money_mary_hypothesis = 1803

# the hypothesis mentions a specific amount of money that Mary has, which was also referenced in the premise
if money_mary_hypothesis >= money_mary_premise:
    # check if the hypothesis value contradicts the premise of having less than 'money_mary_premise'
    label = "contradiction"
else:
    # the premise gives an upper limit for the amount of money Mary possibly has
    # any amount of money less than 'money_mary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
