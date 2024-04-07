# Premise: Kramer can pack 10 boxes of cigarettes per minute.
# Hypothesis: Kramer can pack more than 10 boxes of cigarettes per minute.
# Golden Label: contradiction

cigarettes_packed_premise = 10
cigarettes_packed_hypothesis = 10

# the hypothesis talks about the number of cigarettes boxes Kramer can pack per minute, referenced also in the premise
if cigarettes_packed_hypothesis != cigarettes_packed_premise:
    # check if the hypothesis value contradicts the exact number 'cigarettes_packed_premise' of boxes that Kramer can pack
    label = "contradiction"
else:
    # the premise gives an exact number for the cigarettes boxes that Kramer can pack
    # the exact number of 'cigarettes_packed_premise' can be explicitly entailed from the premise
    label = "entailment"

print(label)

