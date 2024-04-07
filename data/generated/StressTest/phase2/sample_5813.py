# Premise: Sean, who weighs 200 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Hypothesis: Sean, who weighs 100 pounds, is in the elevator with two packages weighing 150 pounds and 280 pounds.
# Golden Label: contradiction

sean_weight_premise = 200
sean_weight_hypothesis = 100
package1_weight = 150
package2_weight = 280

# the hypothesis refers to Sean's weight and the weights of two packages mentioned in the premise
if sean_weight_premise != sean_weight_hypothesis:
    # check if the hypothesis value for Sean's weight contradicts the premise
    label = "contradiction"
elif package1_weight != 150 or package2_weight != 280:
    # check if the weights of the packages in the hypothesis contradict the weights reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, it is neutral as no entailment could be made from the premise
    label = "neutral"

print(label)

