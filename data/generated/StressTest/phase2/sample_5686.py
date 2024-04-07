# Premise: Sean, who weighs less than 700 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Hypothesis: Sean, who weighs 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Golden Label: neutral

sean_weight_premise = 700
sean_weight_hypothesis = 200
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis refers to Sean's weight and the weight of two packages mentioned in the premise
if sean_weight_hypothesis >= sean_weight_premise:
    # check if the hypothesis value of Sean's weight contradicts the estimate of less than 'sean_weight_premise'
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise or package2_weight_hypothesis != package2_weight_premise:
    # check if the weight of either of the two packages in the hypothesis contradicts the weight of the corresponding package reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

