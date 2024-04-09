oranges_premise = 45.0
oranges_per_bag_premise = 23.0
bags_hypothesis = 1.4

# the hypothesis refers to the number of bags, which can be inferred from the premise
# compute the total number of bags in the premise
bags_premise = oranges_premise / oranges_per_bag_premise
if bags_hypothesis!= bags_premise:
    # check if the number of bags in the hypothesis contradicts the number of bags inferred from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
