# Premise: Sean, who weighs less than 800 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Hypothesis: Sean, who weighs 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Golden Label: neutral

sean_weight_premise = 800
sean_weight_hypothesis = 200
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis discusses Sean's weight and the weight of the two packages, which are also mentioned in the premise
if sean_weight_hypothesis >= sean_weight_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sean_weight_premise'
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise or package2_weight_hypothesis != package2_weight_premise:
    # check if the weights of the packages in the hypothesis contradict the weights of the packages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of Sean
    # any weight of Sean less than 'sean_weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

