# Define the variables for the premise
lunch_cakes_premise = 5.0
dinner_cakes_premise = 6.0
yesterday_cakes_premise = 3.0
total_cakes_hypothesis = 14.0

# Calculate the total cakes served in the premise
total_cakes_premise = lunch_cakes_premise + dinner_cakes_premise + yesterday_cakes_premise

# Check if the total cakes in the hypothesis contradicts the total cakes in the premise
if total_cakes_hypothesis!= total_cakes_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
