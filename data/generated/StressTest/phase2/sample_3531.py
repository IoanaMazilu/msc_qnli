# Premise: If Henry were to add 5 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Hypothesis: If Henry were to add less than 7 gallons of water to a tank that is already 3/4 full of water, the tank would be 7/8 full.
# Golden Label: entailment

water_added_premise = 5
water_added_hypothesis = 7

# the hypothesis refers to the amount of water added to the tank, mentioned in the premise
if water_added_hypothesis <= water_added_premise:
    # check if the hypothesis value contradicts the reported amount of water added in the premise
    label = "contradiction"
else:
    # the premise gives an exact amount of water that needs to be added to reach 7/8 of the tank
    # any amount of water less than 'water_added_hypothesis' contradicts the premise
    label = "neutral"

print(label)

