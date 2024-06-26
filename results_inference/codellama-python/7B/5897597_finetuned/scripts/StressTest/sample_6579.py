sean_weight_premise = 200
sean_weight_hypothesis = 800
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis refers to the weight of Sean and the packages mentioned in the premise
if sean_weight_premise > sean_weight_hypothesis:
    # check if the weight of Sean in the premise contradicts the weight of Sean in the hypothesis
    label = "contradiction"
elif package1_weight_premise!= package1_weight_hypothesis or package2_weight_premise!= package2_weight_hypothesis:
    # check if the weight of the packages in the premise contradicts the weight of the packages in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
