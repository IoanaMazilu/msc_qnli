# Premise: In 21 years John will be twice as old as Wilson will be then.
# Hypothesis: In less than 51 years John will be twice as old as Wilson will be then.
# Golden Label: entailment

years_premise = 21
years_hypothesis = 51

# the hypothesis refers to a future time when John will be twice as old as Wilson
# this is directly compared to a similar statement in the premise
if years_hypothesis < years_premise:
    # check if the hypothesis time contradicts the time stated in the premise
    label = "contradiction"
elif years_hypothesis == years_premise:
    # if the time in the hypothesis matches the time in the premise, we can infer entailment
    label = "entailment"
else:
    # any time longer than 'years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

