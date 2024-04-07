# Premise: In 3 years John will be twice as old as Frank.
# Hypothesis: In less than 6 years John will be twice as old as Frank.
# Golden Label: entailment

years_premise = 3
years_hypothesis = 6

# the hypothesis talks about when John will be twice as old as Frank, mentioned also in the premise
if years_hypothesis < years_premise:
    # check if the 'years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
elif years_hypothesis > years_premise:
    # the premise gives a specific number of years for when John will be twice as old as Frank
    # any number of years less than 'years_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis years and premise years are equal, we can infer entailment
    label = "entailment"

print(label)

