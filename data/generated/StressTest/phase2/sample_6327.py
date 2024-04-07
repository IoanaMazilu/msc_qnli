# Premise: Kramer can pack 10 boxes of cigarettes per minute.
# Hypothesis: Kramer can pack less than 20 boxes of cigarettes per minute.
# Golden Label: entailment

boxes_packed_premise = 10
boxes_packed_hypothesis = 20

# the hypothesis talks about the number of boxes Kramer can pack per minute, also referenced in the premise
if boxes_packed_premise >= boxes_packed_hypothesis:
    # check if the premise value contradicts the estimate of less than 'boxes_packed_hypothesis'
    label = "contradiction"
else:
    # the premise specifies the exact number of boxes Kramer can pack
    # any number of boxes less than 'boxes_packed_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

