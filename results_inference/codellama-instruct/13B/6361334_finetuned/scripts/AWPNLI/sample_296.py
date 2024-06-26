total_members_premise = 5.0
missing_members_premise = 2.0
points_per_member_premise = 6.0

# the hypothesis refers to the total number of points scored, which are also mentioned in the premise
# compute the total number of points scored from the premise
total_points_premise = total_members_premise * points_per_member_premise
if total_points_premise!= 18.0:
    # check if the number of points in the hypothesis contradicts the number of points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
