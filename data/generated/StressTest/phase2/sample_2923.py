# Premise: Sean, who weighs less than 300 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Hypothesis: Sean, who weighs 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Golden Label: neutral

sean_weight_premise = 300
sean_weight_hypothesis = 200
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis provides a specific weight for Sean, while the premise only gives an estimate of less than 'sean_weight_premise'
if sean_weight_hypothesis >= sean_weight_premise:
    # check if the hypothesis value contradicts the premise's estimate of Sean's weight
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise or package2_weight_hypothesis != package2_weight_premise:
    # check if the weights of the packages in the hypothesis contradict the weights of the packages in the premise
    label = "contradiction"
else:
    # the specific weight of Sean in the hypothesis does not contradict the premise's estimate
    # but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

