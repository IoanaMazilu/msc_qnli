matched_gloves_premise = 20
matched_gloves_hypothesis = 20

# the hypothesis talks about the number of matched gloves Andy has, referenced also in the premise
if matched_gloves_hypothesis >= matched_gloves_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
