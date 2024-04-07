# Premise: If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of 62 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: contradiction

pens_purchased_premise = 12
pens_purchased_hypothesis = 62

# The hypothesis talks about the number of pens purchased by Elena, referenced also in the premise.
if pens_purchased_premise != pens_purchased_hypothesis:
    # Check if the number of pens mentioned in the hypothesis contradicts the number of pens mentioned in the premise.
    label = "contradiction"
else:
    # If the hypothesis number of pens does not contradict the premise one, we can infer entailment.
    label = "entailment"

print(label)

