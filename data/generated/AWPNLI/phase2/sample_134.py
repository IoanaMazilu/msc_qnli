# Premise: 2.0 toucans are sitting on a tree limb and 1.0 more toucan joins them.
# Hypothesis: There are 3.0 toucans in all.
# Golden Label: entailment

sitting_toucans_premise = 2.0
joined_toucans_premise = 1.0
total_toucans_hypothesis = 3.0

# the hypothesis refers to the total number of toucans, which are also mentioned in the premise
# compute the total number of toucans in the premise
total_toucans_premise = sitting_toucans_premise + joined_toucans_premise
if total_toucans_hypothesis != total_toucans_premise:
    # check if the total number of toucans in the hypothesis contradicts the total number of toucans from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

