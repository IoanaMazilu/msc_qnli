# Premise: Today John is 3 times older than Mark.
# Hypothesis: Today John is 5 times older than Mark.
# Golden Label: contradiction

john_age_multiple_premise = 3
john_age_multiple_hypothesis = 5

# the hypothesis refers to the age relation between John and Mark mentioned in the premise
if john_age_multiple_hypothesis != john_age_multiple_premise:
    # check if the age multiple in the hypothesis contradicts the age multiple in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates are the same as the premise ones
    label = "entailment"

print(label)

