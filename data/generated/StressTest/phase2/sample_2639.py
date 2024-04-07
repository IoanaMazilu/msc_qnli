# Premise: How many crayons does Albert have if he buys 2 additional boxes?
# Hypothesis: How many crayons does Albert have if he buys more than 2 additional boxes?
# Golden Label: contradiction

additional_boxes_premise = 2
additional_boxes_hypothesis = 2

# the hypothesis refers to the same number of additional boxes as the premise
if additional_boxes_hypothesis != additional_boxes_premise:
    # check if the number of additional boxes in the hypothesis contradicts the number of additional boxes in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer neutrality
    # since the premise does not provide explicit information to entail the hypothesis
    label = "neutral"

print(label)

