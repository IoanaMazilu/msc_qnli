total_oranges_premise = 45.0
oranges_per_bag_premise = 23.0
total_bags_hypothesis = 1.4

# the hypothesis refers to the total number of bags, which can be computed from the premise
# compute the total number of bags in the premise
total_bags_premise = total_oranges_premise / oranges_per_bag_premise
if total_bags_hypothesis!= total_bags_premise:
    # check if the number of bags in the hypothesis contradicts the number of bags computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
