crayons_birthday_premise = 479.0
crayons_remaining_premise = 134.0
crayons_lost_hypothesis = 345.0

# the hypothesis refers to the number of crayons that have been lost or given away, which are also mentioned in the premise
# compute the total number of crayons lost or given away from the premise
total_crayons_lost_premise = crayons_birthday_premise - crayons_remaining_premise
if total_crayons_lost_hypothesis!= total_crayons_lost_premise:
    # check if the number of crayons lost or given away from the hypothesis contradicts the number of crayons lost or given away from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
