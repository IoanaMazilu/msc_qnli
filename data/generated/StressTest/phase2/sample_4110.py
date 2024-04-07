# Premise: Jason is 4 times older than Bob at present.
# Hypothesis: Jason is less than 6 times older than Bob at present.
# Golden Label: entailment

jason_age_multiple_premise = 4
jason_age_multiple_hypothesis = 6

# the hypothesis refers to the age ratio between Jason and Bob, mentioned in the premise
if jason_age_multiple_hypothesis < jason_age_multiple_premise:
    # check if the hypothesis value contradicts the precise ratio in the premise
    label = "contradiction"
elif jason_age_multiple_hypothesis == jason_age_multiple_premise:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"
else:
    # the premise gives a precise value for the ratio of ages
    # any ratio greater than 'jason_age_multiple_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

