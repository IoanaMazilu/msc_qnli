total_members_premise = 5.0
absent_members_premise = 2.0
points_per_member_premise = 6.0
total_points_hypothesis = 18.0

# the hypothesis refers to the total points scored, which can be computed from the premise
# compute the total points from the premise
total_points_premise = (total_members_premise - absent_members_premise) * points_per_member_premise
if total_points_hypothesis!= total_points_premise:
    # check if the total points in the hypothesis contradicts the total points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
