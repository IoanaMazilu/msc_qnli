total_oranges_premise = 45.0
oranges_per_bag_premise = 23.0
bags_hypothesis = 1.95652173913

# the hypothesis refers to the number of bags, which is derived from the total amount of oranges and the amount per bag in the premise
# compute the number of bags in the premise
bags_premise = total_oranges_premise / oranges_per_bag_premise
if abs(bags_hypothesis - bags_premise) > 0.00001:
    # check if the number of bags in the hypothesis contradicts the number of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
