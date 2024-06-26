crayons_lost_hypothesis = 345.0
crayons_lost_premise = 479.0 - 134.0

if crayons_lost_hypothesis!= crayons_lost_premise:
    # check if the number of crayons lost from the hypothesis contradicts the number of crayons lost from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
