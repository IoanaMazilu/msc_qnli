# Premise: If Elena purchased a total of less than 22 of these pens for $20.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of 12 of these pens for $20.00, how many brand X pens did she purchase?
# Golden Label: neutral

total_pens_premise = 22
total_pens_hypothesis = 12

# the hypothesis refers to the number of pens Elena bought, mentioned in the premise
if total_pens_hypothesis >= total_pens_premise:
    # check if the number of pens 'total_pens_hypothesis' contradicts the estimate of less than 'total_pens_premise'
    label = "contradiction"
elif total_pens_hypothesis < total_pens_premise:
    # the premise gives an estimate for the number of pens bought
    # any number of pens less than 'total_pens_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

