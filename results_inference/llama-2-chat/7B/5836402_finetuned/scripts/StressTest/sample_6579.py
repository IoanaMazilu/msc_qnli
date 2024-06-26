sean_weight_premise = 200
total_weight_packages_premise = 150 + 280
total_weight_packages_hypothesis = 150 + 280

# the hypothesis refers to the total weight of packages mentioned in the premise
if total_weight_packages_hypothesis >= total_weight_packages_premise:
    # check if the estimate of 'total_weight_packages_hypothesis' contradicts the total weight of packages in the premise
    label = "contradiction"
elif sean_weight_premise > 800:
    # check if the weight of Sean in the hypothesis contradicts the weight of Sean in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
