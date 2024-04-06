# Premise: At least one person died in the post-election violence, authorities said.
# Hypothesis: At least one person is dead in post-election violence.
# Golden Label: entailment

deaths_premise = 1
deaths_hypothesis = 1

# the hypothesis mentions at least one death in the post-election violence, which is in the premise
if deaths_hypothesis < deaths_premise:
    # check if the number of deaths in the hypothesis is less than the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the number of deaths in the hypothesis is not less than the number of deaths in the premise, we can infer entailment
    label = "entailment"

print(label)

