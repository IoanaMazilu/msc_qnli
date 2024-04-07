# Premise: loyd wants to fence his Square shaped land of 130 Sqft each side.
# Hypothesis: loyd wants to fence his Square shaped land of less than 130 Sqft each side.
# Golden Label: contradiction

land_side_size_premise = 130
land_side_size_hypothesis = 130

# the hypothesis refers to the size of each side of the land mentioned in the premise
if land_side_size_hypothesis >= land_side_size_premise:
    # check if the hypothesis contradicts the premise about the size of each side of the land
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise about the size of each side of the land, we can infer entailment
    label = "entailment"

print(label)

