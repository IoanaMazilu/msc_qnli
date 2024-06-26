sean_weight_premise = 100
sean_weight_hypothesis = 200
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# The hypothesis is referring to the weight of Sean and the packages mentioned in the premise
if sean_weight_hypothesis <= sean_weight_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'sean_weight_premise'
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise or package2_weight_hypothesis != package2_weight_premise:
    # Check if the weight of the packages in the hypothesis contradicts the weight of the packages in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for Sean's weight
    # Any weight of Sean greater than 'sean_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
