premise = "If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?"
hypothesis = "If Elena purchased a total of more than 12 of these pens for $42.00, how many brand X pens did she purchase?"

# extract the numerical entities from the premise
total_pens_premise = 12
price_premise = 42.00

# extract the numerical entities from the hypothesis
total_pens_hypothesis = 12
price_hypothesis = 42.00

# check if the hypothesis value contradicts the premise estimate
if total_pens_hypothesis <= total_pens_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pens
    # any number of pens greater than 'total_pens_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
