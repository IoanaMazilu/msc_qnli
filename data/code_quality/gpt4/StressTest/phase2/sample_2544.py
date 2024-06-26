earnings_rise_premise = 20
earnings_rise_hypothesis = 30
earnings_premise = 560
earnings_hypothesis = 560

# the hypothesis refers to the same potential earnings of Albert and the percentage rise, as mentioned in the premise
if earnings_premise != earnings_hypothesis:
    # check if the potential earnings in the hypothesis contradicts the potential earnings mentioned in the premise
    label = "contradiction"
elif earnings_rise_hypothesis < earnings_rise_premise:
    # check if the percentage rise in the hypothesis contradicts the percentage rise mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the potential earnings and percentage rise
    # any percentage rise less than 'earnings_rise_hypothesis' and equal earnings is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
