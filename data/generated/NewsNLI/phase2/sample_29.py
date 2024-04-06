# Premise: Coover was 94.
# Hypothesis: He was 94.
# Golden Label: entailment

age_premise = 94
age_hypothesis = 94

# the hypothesis refers to the age of a person, which is also mentioned in the premise
if age_hypothesis != age_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

