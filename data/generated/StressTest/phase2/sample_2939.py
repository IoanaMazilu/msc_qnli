# Premise: If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of less than 12 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: contradiction

pens_purchased_premise = 12
pens_purchased_hypothesis = 12

# the hypothesis mentions the same number of pens purchased as the premise
if pens_purchased_hypothesis >= pens_purchased_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)

