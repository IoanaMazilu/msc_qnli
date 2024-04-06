# Premise: Robin has 18.0 pieces of gum and her brother gave her 44.0 more pieces.
# Hypothesis: Robin has 60.0 pieces of gum now.
# Golden Label: contradiction

gum_robin_premise = 18.0
gum_brother_premise = 44.0
total_gum_hypothesis = 60.0

# the hypothesis refers to the total number of gum pieces Robin has, which are also mentioned in the premise
# calculate the total number of gum pieces in the premise
total_gum_premise = gum_robin_premise + gum_brother_premise
if total_gum_hypothesis != total_gum_premise:
    # check if the total number of gum pieces in the hypothesis contradicts the total number of gum pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

