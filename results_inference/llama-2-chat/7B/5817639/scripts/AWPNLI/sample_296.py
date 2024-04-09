# Define variables for premise and hypothesis values
total_members_premise = 5.0
members_didnt_show_up_hypothesis = 2.0
points_per_member_hypothesis = 6.0
total_points_hypothesis = 0

# Calculate the total number of members that showed up
total_members_showed_up = total_members_premise - members_didnt_show_up_hypothesis

# Calculate the total points scored by the members that showed up
points_scored_by_showed_up = total_members_showed_up * points_per_member_hypothesis

# Check if the total points scored contradict the hypothesis
if points_scored_by_showed_up!= total_points_hypothesis:
    label = "contradiction"
else:
    # If the total points scored do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
