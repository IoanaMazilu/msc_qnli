# Define variables for the numerical entities in the premise
total_members_premise = 5.0
members_absent_premise = 2.0
points_per_member_premise = 6.0

# Define variables for the numerical entities in the hypothesis
total_points_hypothesis = 18.0

# Calculate the total number of points scored by the team
total_points_premise = total_members_premise * points_per_member_premise

# Check if the total number of points scored by the team contradicts the estimate in the hypothesis
if total_points_hypothesis!= total_points_premise:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
