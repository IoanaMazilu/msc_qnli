# Premise: United States Daily US Deficit For 2/13/2013: $23.3B.
# Hypothesis: Daily US Deficit For 2/14/2013: $6.2B.
# Golden Label: neutral

deficit_premise = 23.3
date_premise = "2/13/2013"
deficit_hypothesis = 6.2
date_hypothesis = "2/14/2013"

# the hypothesis and premise mention the US daily deficit and the date
if date_premise != date_hypothesis:
    # the dates in the premise and hypothesis are different, so one does not contradict the other
    label = "neutral"
elif deficit_premise != deficit_hypothesis:
    # if the dates were the same, then the deficits should have also been the same
    label = "contradiction"
else:
    # if the dates and the deficits in the premise and hypothesis are the same, then the hypothesis can be entailed from the premise
    label = "entailment"

print(label)

