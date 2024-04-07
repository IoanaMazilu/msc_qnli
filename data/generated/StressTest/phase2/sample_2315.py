# Premise: Today John is 3 times older than Mark.
# Hypothesis: Today John is 4 times older than Mark.
# Golden Label: contradiction

john_age_multiple_premise = 3
john_age_multiple_hypothesis = 4

# the hypothesis refers to the age difference between John and Mark, also mentioned in the premise
if john_age_multiple_hypothesis != john_age_multiple_premise:
    # check if the age multiple in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # if the age multiples mentioned in the premise and the hypothesis match, we can infer entailment
    label = "entailment"

print(label)

