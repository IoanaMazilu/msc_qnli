# Premise: Andy has 20 pairs of matched gloves.
# Hypothesis: Andy has more than 20 pairs of matched gloves.
# Golden Label: contradiction

matched_gloves_premise = 20
matched_gloves_hypothesis = 20

# the hypothesis talks about the number of matched gloves Andy has, referenced also in the premise
if matched_gloves_hypothesis != matched_gloves_premise:
    # check if the hypothesis value contradicts the definite number 'matched_gloves_premise'
    label = "contradiction"
else:
    # the premise gives a definite number for the pairs of matched gloves Andy has
    # the same number of matched gloves is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

