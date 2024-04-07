# Premise: How many different ways can you arrange the 4 dancers in a line if Anne must be first or second.
# Hypothesis: How many different ways can you arrange the more than 1 dancers in a line if Anne must be first or second.
# Golden Label: entailment

dancers_premise = 4
dancers_hypothesis = 1

# the hypothesis talks about the number of dancers, referenced also in the premise
if dancers_hypothesis > dancers_premise:
    # check if the hypothesis value contradicts the number of dancers in the premise
    label = "contradiction"
elif dancers_hypothesis < dancers_premise:
    # check if the number of dancers in the hypothesis is less than the number of dancers in the premise
    label = "entailment"
else:
    # if the hypothesis value and premise value are equal, we can infer entailment
    label = "entailment"

print(label)

