total_pens_premise = 12
total_pens_hypothesis = 22

# The hypothesis talks about the total number of pens Elena purchased, also mentioned in the premise
if total_pens_hypothesis < total_pens_premise:
    # check if the hypothesis value contradicts the total number of pens mentioned in the premise
    label = "contradiction"
elif total_pens_hypothesis == total_pens_premise:
    # check if the hypothesis value is exactly the same with the premise
    label = "entailment"
else:
    # the hypothesis gives an estimate for the total number of pens
    # any total number of pens less than 'total_pens_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
