# Premise: Sujeet joined him 2 months later, investing Rs.
# Hypothesis: Sujeet joined him less than 6 months later, investing Rs.
# Golden Label: entailment

months_joined_premise = 2
months_joined_hypothesis = 6

# the hypothesis refers to the time Sujeet joined him, also mentioned in the premise
if months_joined_hypothesis < months_joined_premise:
    # check if the hypothesis value contradicts the exact time mentioned in the premise
    label = "contradiction"
elif months_joined_hypothesis == months_joined_premise:
    # if the hypothesis value matches the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives an exact time, any time less than 'months_joined_hypothesis' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

