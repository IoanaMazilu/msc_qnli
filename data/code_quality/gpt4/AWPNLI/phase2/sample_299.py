points_per_bag_premise = 5.0
total_bags_premise = 11.0
not_recycled_bags_premise = 2.0
total_points_hypothesis = 44.0

# the hypothesis refers to the total points earned, which can be computed from the premise
# compute the total points earned in the premise
total_points_premise = (total_bags_premise - not_recycled_bags_premise) * points_per_bag_premise

if total_points_hypothesis != total_points_premise:
    # check if the number of points in the hypothesis contradicts the number of points from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
