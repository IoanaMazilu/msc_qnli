total_members_premise = 5.0
absent_members_premise = 2.0
points_per_member_premise = 6.0
total_points_hypothesis = 18.0

# the hypothesis refers to the total points scored, which can be calculated from the premise
# compute the total points scored in the premise
total_points_premise = total_members_premise * points_per_member_premise - absent_members_premise * points_per_member_premise
if total_points_hypothesis!= total_points_premise:
    # check if the total points in the hypothesis contradicts the total points calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
