oranges_premise = 45.0
oranges_per_bag_premise = 23.0
bags_hypothesis = 1.95652173913

# the hypothesis refers to the number of bags, which is also mentioned in the premise
# compute the total number of bags in the premise
total_bags_premise = oranges_premise / oranges_per_bag_premise
if bags_hypothesis!= total_bags_premise:
    # check if the number of bags in the hypothesis contradicts the number of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
