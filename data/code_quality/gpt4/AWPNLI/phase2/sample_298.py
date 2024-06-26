points_per_bag_premise = 5.0
total_bags_premise = 11.0
unrecycled_bags_premise = 2.0
total_points_hypothesis = 45.0

# the hypothesis refers to the total points earned, which is based on the number of bags recycled in the premise
# compute the total number of bags recycled and the corresponding points earned in the premise
recycled_bags_premise = total_bags_premise - unrecycled_bags_premise
total_points_premise = recycled_bags_premise * points_per_bag_premise
if total_points_hypothesis != total_points_premise:
    # check if the total points in the hypothesis contradicts the total points calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
