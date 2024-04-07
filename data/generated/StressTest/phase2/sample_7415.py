# Premise: loyd wants to fence his Square shaped land of 120 Sqft each side.
# Hypothesis: loyd wants to fence his Square shaped land of 220 Sqft each side.
# Golden Label: contradiction

land_size_premise = 120
land_size_hypothesis = 220

# the hypothesis talks about the size of the land that is also mentioned in the premise
if land_size_hypothesis != land_size_premise:
    # check if the size of the land in the hypothesis contradicts the size of the land in the premise
    label = "contradiction"
else:
    # if the size of the land in the hypothesis does not contradict the size of the land in the premise, we can infer entailment
    label = "entailment"

print(label)

