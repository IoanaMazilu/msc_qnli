# Premise: Sharapova's semifinal opponent is unseeded German Sabine Lisicki, who continued her remarkable run of form by defeating Marion Bartoli of France in three sets.
# Hypothesis: Sharapova next faces German Sabine Lisicki, who defeats Marion Bartoli in three sets.
# Golden Label: entailment

sets_premise = 3
sets_hypothesis = 3

# the hypothesis mentions the number of sets in which the match was played, which is also referenced in the premise
if sets_hypothesis != sets_premise:
    # check if the number of sets in the hypothesis contradicts the number of sets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

