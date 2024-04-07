# Premise: If Elena purchased a total of less than 82 of these pens for $40.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of 12 of these pens for $40.00, how many brand X pens did she purchase?
# Golden Label: neutral

total_pens_premise = 82
total_pens_hypothesis = 12
cost_premise = 40.0
cost_hypothesis = 40.0

# the hypothesis refers to the number and cost of the purchased pens mentioned in the premise
if total_pens_hypothesis >= total_pens_premise:
    # check if the hypothesis value contradicts the premise of less than 'total_pens_premise' pens
    label = "contradiction"
elif cost_hypothesis != cost_premise:
    # check if the cost in the premise contradicts the cost in the hypothesis
    label = "contradiction"
else:
    # any number of pens less than 'total_pens_premise' and the same cost as in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

