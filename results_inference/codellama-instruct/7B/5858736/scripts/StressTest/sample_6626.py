# Define variables for the premise
sheep_num_premise = 6
horse_num_premise = 7
horse_food_per_day_premise = 230
total_food_per_day_premise = 12880

# Define variables for the hypothesis
sheep_num_hypothesis = 0
horse_num_hypothesis = 0
horse_food_per_day_hypothesis = 0
total_food_per_day_hypothesis = 0

# Calculate the number of sheep and horses in the farm based on the premise
sheep_num_hypothesis = total_food_per_day_premise / (horse_food_per_day_premise * horse_num_premise)
horse_num_hypothesis = total_food_per_day_premise / (horse_food_per_day_premise * sheep_num_premise)

# Calculate the number of horses and sheep in the farm based on the hypothesis
sheep_num_hypothesis = total_food_per_day_hypothesis / (horse_food_per_day_hypothesis * horse_num_hypothesis)
horse_num_hypothesis = total_food_per_day_hypothesis / (horse_food_per_day_hypothesis * sheep_num_hypothesis)

# Check if the hypothesis values contradict the premise
if sheep_num_hypothesis > sheep_num_premise or horse_num_hypothesis > horse_num_premise:
    label = "contradiction"
elif sheep_num_hypothesis < sheep_num_premise or horse_num_hypothesis < horse_num_premise:
    label = "neutral"
else:
    label = "entailment"

print(label)
