sean_weight_premise = 200
sean_weight_hypothesis = 800
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis refers to the weight of Sean and the packages mentioned in the premise
if sean_weight_hypothesis <= sean_weight_premise:
    # check if the estimate of'sean_weight_hypothesis' contradicts the weight of Sean in the premise
    label = "contradiction"
elif package1_weight_hypothesis!= package1_weight_premise or package2_weight_hypothesis!= package2_weight_premise:
    # check if the weights of the packages in the hypothesis contradict the weights of the packages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)