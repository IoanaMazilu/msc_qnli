# Premise: If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of more than 12 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: contradiction

pens_purchased_premise = 12
pens_purchased_hypothesis = 12

# The hypothesis refers to the number of purchased pens mentioned in the premise
if pens_purchased_hypothesis < pens_purchased_premise:
    # Check if the number of pens purchased in the hypothesis contradicts the number of pens purchased in the premise
    label = "contradiction"
elif pens_purchased_hypothesis == pens_purchased_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only the exact number of pens purchased
    # any number of pens greater than 'pens_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

