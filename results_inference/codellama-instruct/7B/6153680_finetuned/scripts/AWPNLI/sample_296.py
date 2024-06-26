# Define the variables
total_members = 5.0
missing_members = 2.0
member_points = 6.0
total_points = 18.0

# Calculate the total points for the team
total_points_calc = total_members * member_points

# Check if the total points in the hypothesis match the calculated total points
if total_points_calc!= total_points:
    # If the total points in the hypothesis do not match the calculated total points, we have a contradiction
    label = "contradiction"
else:
    # If the total points in the hypothesis match the calculated total points, we have entailment
    label = "entailment"

print(label)
