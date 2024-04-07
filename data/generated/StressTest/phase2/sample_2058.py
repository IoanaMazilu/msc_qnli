# Premise: If Elena purchased a total of 12 of these pens for $40.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of less than 82 of these pens for $40.00, how many brand X pens did she purchase?
# Golden Label: entailment

total_pens_purchased_premise = 12
total_pens_purchased_hypothesis = 82

# The hypothesis refers to the total number of pens purchased by Elena, which is also mentioned in the premise.
if total_pens_purchased_hypothesis <= total_pens_purchased_premise:
    # Check if the hypothesis value contradicts the number of total pens purchased in the premise.
    label = "contradiction"
elif total_pens_purchased_hypothesis > total_pens_purchased_premise:
    # The premise gives an exact number of total pens purchased.
    # Any number of total pens purchased greater than 'total_pens_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise.
    label = "neutral"

print(label)

