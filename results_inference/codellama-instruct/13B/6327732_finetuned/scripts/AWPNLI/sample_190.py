bought_crayons_premise = 479.0
left_crayons_premise = 134.0
lost_or_given_crayons_hypothesis = 345.0

# the hypothesis refers to the number of crayons that were lost or given away, which are also mentioned in the premise
# compute the total number of crayons in the premise
total_crayons_premise = bought_crayons_premise + left_crayons_premise
if total_crayons_hypothesis > total_crayons_premise:
    # check if the number of crayons in the hypothesis contradicts the number of crayons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
