sean_weight_premise = 400
sean_weight_hypothesis = 200
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis gives specific values for Sean's weight and the weights of the packages, which are also mentioned in the premise
if sean_weight_hypothesis >= sean_weight_premise:
    # check if the hypothesis value contradicts the estimate of Sean's weight being less than 'sean_weight_premise'
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise or package2_weight_hypothesis != package2_weight_premise:
    # check if the weights of the packages in the hypothesis contradict the weights mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Sean's weight
    # any weight less than 'sean_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
