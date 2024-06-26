matched_gloves_premise = 20
matched_gloves_hypothesis = 20

# the hypothesis refers to the number of pairs of matched gloves Andy has, which is also mentioned in the premise
if matched_gloves_hypothesis!= matched_gloves_premise:
    # check if the number of pairs of matched gloves in the hypothesis contradicts the number of pairs of matched gloves in the premise
    label = "contradiction"
else:
    # if the number of pairs of matched gloves in the hypothesis does not contradict the number of pairs of matched gloves in the premise, we can infer entailment
    label = "entailment"

print(label)
