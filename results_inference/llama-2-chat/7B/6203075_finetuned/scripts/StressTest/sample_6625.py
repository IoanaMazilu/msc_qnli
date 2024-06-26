# Define the variables
sheep_horses_premise = 1 / 7
sheep_horses_hypothesis = 6 / 7
horse_food_premise = 230
horse_food_hypothesis = 230
total_food_premise = 12880
total_food_hypothesis = 12880

# Define the equation for the hypothesis
sheep_horses_hypothesis = sheep_horses_premise * (total_food_hypothesis / total_food_premise)

# Check if the hypothesis values contradict the premise
if sheep_horses_hypothesis!= sheep_horses_premise:
    label = "contradiction"
elif horse_food_hypothesis!= horse_food_premise:
    label = "contradiction"
elif total_food_hypothesis!= total_food_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
