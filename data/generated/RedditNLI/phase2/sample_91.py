# Premise: Oxfam says richest one percent to own more than rest by 2016.
# Hypothesis: Richest 1% To Own More Than Half Worlds Wealth By 2016 Oxfam.
# Golden Label: entailment

richest_percentage_premise = 1
richest_percentage_hypothesis = 1

# the hypothesis and premise both mention the percentage of the richest people in the world
if richest_percentage_premise != richest_percentage_hypothesis:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage in the hypothesis does not contradict the percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

