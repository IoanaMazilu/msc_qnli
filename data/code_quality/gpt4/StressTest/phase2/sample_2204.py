packages_pens_premise = 6
packages_pens_hypothesis = 7

# the hypothesis refers to the number of pen packages Steve bought, which is also mentioned in the premise
if packages_pens_hypothesis != packages_pens_premise:
    # check if the number of packages in the hypothesis contradicts the number of packages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)