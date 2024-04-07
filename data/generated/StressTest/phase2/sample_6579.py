# Premise: Sean, who weighs 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Hypothesis: Sean, who weighs less than 800 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Golden Label: entailment

sean_weight_premise = 200
sean_weight_hypothesis = 800
package1_weight_premise = 150
package1_weight_hypothesis = 150
package2_weight_premise = 280
package2_weight_hypothesis = 280

# The hypothesis refers to the weights of Sean and the two packages mentioned in the premise
if sean_weight_premise > sean_weight_hypothesis:
    # Check if the weight of Sean in the hypothesis contradicts the weight of Sean in the premise
    label = "contradiction"
elif package1_weight_premise != package1_weight_hypothesis or package2_weight_premise != package2_weight_hypothesis:
    # Check if the weights of the packages in the hypothesis contradict the weights of the packages in the premise
    label = "contradiction"
else:
    # If the weights in the hypothesis do not contradict the weights in the premise, we can infer entailment
    label = "entailment"

print(label)

