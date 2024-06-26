sean_weight_premise = 200
sean_weight_hypothesis = 800
package_weight_premise_1 = 150
package_weight_premise_2 = 280
package_weight_hypothesis_1 = 150
package_weight_hypothesis_2 = 280

# the hypothesis refers to the weight of Sean and the packages mentioned in the premise
if sean_weight_premise > sean_weight_hypothesis:
    # check if the estimate of'sean_weight_hypothesis' contradicts the weight of Sean in the premise
    label = "contradiction"
elif package_weight_premise_1!= package_weight_hypothesis_1 or package_weight_premise_2!= package_weight_hypothesis_2:
    # check if the weight of the packages in the hypothesis contradicts the weight of the packages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
