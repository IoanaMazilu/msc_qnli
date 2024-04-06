# Premise: There are 64.0 pigs in the barn and 86.0 more pigs come to join them.
# Hypothesis: There are 149.0 pigs now.
# Golden Label: contradiction

pigs_premise = 64.0
pigs_join_premise = 86.0
pigs_hypothesis = 149.0

# the hypothesis is about the total number of pigs, which is also specified in the premise
# calculate the total number of pigs from the premise
total_pigs_premise = pigs_premise + pigs_join_premise
if pigs_hypothesis != total_pigs_premise:
    # check if the total number of pigs in the hypothesis contradicts the total number of pigs from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

