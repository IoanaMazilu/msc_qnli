toucans_premise = 2.0
joined_toucan_premise = 1.0
total_toucans_hypothesis = 5.0

# the hypothesis refers to the total number of toucans, which are also mentioned in the premise
# compute the total number of toucans in the premise
total_toucans_premise = toucans_premise + joined_toucan_premise
if total_toucans_hypothesis != total_toucans_premise:
    # check if the total number of toucans in the hypothesis contradicts the total number of toucans from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)