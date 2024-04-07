# Premise: If Elena purchased a total of 12 of these pens for $42.00, how many brand X pens did she purchase?
# Hypothesis: If Elena purchased a total of less than 42 of these pens for $42.00, how many brand X pens did she purchase?
# Golden Label: entailment

total_pens_premise = 12
total_pens_hypothesis = 42

# the hypothesis makes a supposition about the total number of pens purchased by Elena, also mentioned in the premise
if total_pens_hypothesis <= total_pens_premise:
    # check if the hypothesis value contradicts the exact number of 'total_pens_premise'
    label = "contradiction"
else:
    # the premise gives the exact number of pens purchased
    # any number of pens less than 'total_pens_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

