years_premise = 5
years_hypothesis = 4

# the hypothesis talks about the same situation as the premise, but with a different time frame
if years_hypothesis != years_premise:
    # check if the hypothesis timeline contradicts the premise timeline
    label = "contradiction"
else:
    # if the hypothesis timeline does not contradict the premise timeline, we can infer entailment
    label = "entailment"

print(label)
