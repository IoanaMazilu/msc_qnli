# Premise: If side AC = less than 30 units, what is the area of the triangle?
# Hypothesis: If side AC = 20 units, what is the area of the triangle?
# Golden Label: neutral

side_ac_premise = 30
side_ac_hypothesis = 20

# the hypothesis makes a statement about the length of side AC of a triangle, mentioned also in the premise
if side_ac_hypothesis >= side_ac_premise:
    # check if the length of side AC in the hypothesis contradicts the premise that it should be less than 'side_ac_premise'
    label = "contradiction"
elif side_ac_hypothesis < side_ac_premise:
    # the premise specifies that side AC should be less than 'side_ac_premise'
    # the hypothesis gives a specific value which is less than 'side_ac_premise', so it can be explicitly entailed from the premise
    label = "entailment"
else:
    # the hypothesis makes a statement consistent with the premise, but it doesn't provide sufficient information to be fully entailed from the premise
    label = "neutral"

print(label)

