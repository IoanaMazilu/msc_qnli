# Premise: loyd wants to fence his Square shaped land of less than 230 Sqft each side.
# Hypothesis: loyd wants to fence his Square shaped land of 130 Sqft each side.
# Golden Label: neutral

land_size_premise = 230
land_size_hypothesis = 130

# the hypothesis refers to the size of the land mentioned in the premise
if land_size_hypothesis >= land_size_premise:
    # check if the size of 'land_size_hypothesis' contradicts the size of the land in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the land
    # any land size less than 'land_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

