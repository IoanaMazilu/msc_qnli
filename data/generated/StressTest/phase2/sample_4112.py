# Premise: Jason is 4 times older than Bob at present.
# Hypothesis: Jason is 3 times older than Bob at present.
# Golden Label: contradiction

jason_age_multiple_premise = 4
jason_age_multiple_hypothesis = 3

# the hypothesis refers to the age relationship between Jason and Bob mentioned in the premise
if jason_age_multiple_hypothesis != jason_age_multiple_premise:
    # check if the age multiple in the hypothesis contradicts the age multiple reported in the premise
    label = "contradiction"
else:
    # if the age multiple in the hypothesis does not contradict the age multiple in the premise, we can infer entailment
    label = "entailment"

print(label)

