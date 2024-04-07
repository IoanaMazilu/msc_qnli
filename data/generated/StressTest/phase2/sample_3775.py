# Premise: However, less than 65 percent of the sales representatives prefer to stay at Hotel XYZ and 45 percent prefer to stay at Hotel ABC.
# Hypothesis: However, 55 percent of the sales representatives prefer to stay at Hotel XYZ and 45 percent prefer to stay at Hotel ABC.
# Golden Label: neutral

hotel_xyz_preference_premise = 65
hotel_xyz_preference_hypothesis = 55
hotel_abc_preference_premise = 45
hotel_abc_preference_hypothesis = 45

# The hypothesis refers to the percentage of sales representatives who prefer Hotel XYZ and Hotel ABC mentioned in the premise
if hotel_xyz_preference_hypothesis >= hotel_xyz_preference_premise:
    # Check if the percentage of sales representatives who prefer Hotel XYZ in the hypothesis contradicts the premise
    label = "contradiction"
elif hotel_abc_preference_hypothesis != hotel_abc_preference_premise:
    # Check if the percentage of sales representatives who prefer Hotel ABC in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the percentage of sales representatives who prefer Hotel XYZ
    # The percentage in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

