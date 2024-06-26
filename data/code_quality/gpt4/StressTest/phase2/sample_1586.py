advance_premise = 20000
advance_hypothesis = 10000

# the hypothesis and premise both refer to the money advanced by Sravan after 8 months
if advance_hypothesis > advance_premise:
    # check if the hypothesis value contradicts the amount advanced by Sravan as per the premise
    label = "contradiction"
elif advance_hypothesis == advance_premise:
    # check if the hypothesis value is the same as the amount advanced by Sravan as per the premise
    label = "entailment"
else:
    # any amount less than 'advance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
