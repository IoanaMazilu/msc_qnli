sean_weight_premise = 200
sean_weight_hypothesis = 300
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis refers to the weight of Sean and the packages which are mentioned in the premise
if sean_weight_hypothesis != sean_weight_premise:
    # check if the weight of Sean in the hypothesis contradicts his weight reported in the premise
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise:
    # check if the weight of the first package in the hypothesis contradicts its weight reported in the premise
    label = "contradiction"
elif package2_weight_hypothesis != package2_weight_premise:
    # check if the weight of the second package in the hypothesis contradicts its weight reported in the premise
    label = "contradiction"
else:
    # if the weights in the hypothesis do not contradict the weights mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
