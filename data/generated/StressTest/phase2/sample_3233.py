# Premise: Andy has 20 pairs of matched gloves.
# Hypothesis: Andy has 40 pairs of matched gloves.
# Golden Label: contradiction

matched_gloves_premise = 20
matched_gloves_hypothesis = 40

# the hypothesis talks about the number of matched gloves Andy has, which is also mentioned in the premise
if matched_gloves_hypothesis != matched_gloves_premise:
    # check if the number of matched gloves in the hypothesis contradicts the number of matched gloves mentioned in the premise
    label = "contradiction"
else:
    # if the number of matched gloves in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)

