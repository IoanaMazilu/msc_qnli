# Premise: I have 4.0 pencil boxes, and I fill each box with 648.0 pencils.
# Hypothesis: I will have 2592.0 pencils.
# Golden Label: entailment

pencil_boxes_premise = 4.0
pencils_per_box_premise = 648.0
total_pencils_hypothesis = 2592.0

# the hypothesis refers to the total number of pencils, which can be calculated from the premise
# compute the total number of pencils in the premise
total_pencils_premise = pencil_boxes_premise * pencils_per_box_premise
if total_pencils_hypothesis != total_pencils_premise:
    # check if the total number of pencils in the hypothesis contradicts the calculated total pencils from the premise
    label = "contradiction"
else:
    # if the calculated total pencils from the premise matches the total pencils in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

