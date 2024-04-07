# Premise: loyd wants to fence his Square shaped land of less than 320 Sqft each side.
# Hypothesis: loyd wants to fence his Square shaped land of 120 Sqft each side.
# Golden Label: neutral

land_size_premise = 320
land_size_hypothesis = 120

# the hypothesis refers to the size of the land mentioned in the premise
if land_size_hypothesis >= land_size_premise:
    # check if the size of the land mentioned in the hypothesis contradicts the size of the land in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the land
    # any size of land less than 'land_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

