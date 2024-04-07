# Premise: If Elena purchased a total of 10 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of less than 30 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: entailment

total_pens_purchased_premise = 10
total_pens_purchased_hypothesis = 30
cost_premise = 42.00
cost_hypothesis = 42.00

# the hypothesis refers to the total number of pens purchased and their cost mentioned in the premise
if total_pens_purchased_hypothesis < total_pens_purchased_premise:
    # check if the hypothetical total number of pens purchased contradicts the number in the premise
    label = "contradiction"
elif cost_hypothesis != cost_premise:
    # check if the hypothetical cost contradicts the cost in the premise
    label = "contradiction"
else:
    # if the hypothetical values do not contradict the premise's values, we can infer neutral
    # because the premise does not provide enough information to entail the hypothesis
    label = "neutral"

print(label)

