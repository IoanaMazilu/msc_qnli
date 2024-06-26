total_members_premise = 5.0
members_not_showing_up_premise = 2.0
points_per_member_premise = 6.0
total_points_hypothesis = 18.0

# the hypothesis refers to the total points scored, which can be calculated from the premise
# compute the total points scored in the premise
total_points_premise = total_members_premise * points_per_member_premise - (total_members_premise - members_not_showing_up_premise) * points_per_member_premise
print(f"Total points in the premise: {total_points_premise}")

# check if the total points in the hypothesis contradicts the total points in the premise
if total_points_hypothesis!= total_points_premise:
    # if the hypothesis values contradict the premise values, we have a contradiction
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we have entailment
    label = "entailment"

print(f"Label: {label}")
