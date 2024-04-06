# Premise: (CNN) -- Police in Mexico City have detained three people in the mysterious disappearance of 12 people from a nightclub, the city's attorney general said.
# Hypothesis: Police have not said why these three were detained.
# Golden Label: neutral

people_disappeared_premise = 12
people_detained_premise = 3
people_detained_hypothesis = 3

# the hypothesis mentions the number of people detained which matches the number in the premise
# but the hypothesis does not provide a reason for their detention, which is not mentioned in the premise either
# thus we cannot confirm or deny the hypothesis based on the premise
label = "neutral"

print(label)

