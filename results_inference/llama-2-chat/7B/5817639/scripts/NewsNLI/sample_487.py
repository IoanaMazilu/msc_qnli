considering_premise = "considering"
considering_hypothesis = "considering"

# the hypothesis mentions the same action as the premise, but the premise uses the word "considering" which implies a possibility of change
if considering_hypothesis == considering_premise:
    # if the hypothesis and premise are the same, we can infer entailment
    label = "entailment"
elif considering_hypothesis!= considering_premise:
    # if the hypothesis and premise are different, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise are the same but with a different word choice, we can infer neutrality
    label = "neutral"

print(label)
