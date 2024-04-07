# Premise: If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of less than 22 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: entailment

total_pens_purchased_premise = 12
total_pens_purchased_hypothesis = 22

# the hypothesis refers to the total number of pens purchased by Elena, also mentioned in the premise
if total_pens_purchased_hypothesis <= total_pens_purchased_premise:
    # check if the hypothesis value contradicts the number of pens purchased in the premise
    label = "contradiction"
else:
    # the premise gives an exact number for the total pens purchased
    # any number less than 'total_pens_purchased_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

