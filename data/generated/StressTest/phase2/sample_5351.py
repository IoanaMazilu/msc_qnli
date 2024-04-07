# Premise: Sean, who weighs 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Hypothesis: Sean, who weighs more than 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Golden Label: contradiction

sean_weight_premise = 200
sean_weight_hypothesis = 200
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# the hypothesis refers to Sean's weight and the weights of two packages mentioned in the premise
if sean_weight_hypothesis != sean_weight_premise:
    # check if Sean's weight in the hypothesis contradicts Sean's weight reported in the premise
    label = "contradiction"
elif package1_weight_hypothesis != package1_weight_premise or package2_weight_hypothesis != package2_weight_premise:
    # check if the weights of the packages in the hypothesis contradict the weights of the packages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

