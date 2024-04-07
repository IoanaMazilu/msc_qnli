# Premise: loyd wants to fence his Square shaped land of 120 Sqft each side.
# Hypothesis: loyd wants to fence his Square shaped land of less than 320 Sqft each side.
# Golden Label: entailment

land_size_premise = 120
land_size_hypothesis = 320

# the hypothesis is about the size of a square land that is also mentioned in the premise
if land_size_hypothesis <= land_size_premise:
    # check if the hypothesis that the land is less than 'land_size_hypothesis' contradicts the premise's land size
    label = "contradiction"
elif land_size_hypothesis != land_size_premise:
    # check if the hypothesis that the land is exactly 'land_size_hypothesis' contradicts the premise's land size
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

