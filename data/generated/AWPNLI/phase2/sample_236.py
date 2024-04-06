# Premise: 1035.0 pounds of oranges are in 45.0 bags.
# Hypothesis: Each bag contains 23.0 pounds of oranges.
# Golden Label: entailment

total_oranges_premise = 1035.0
total_bags_premise = 45.0
oranges_per_bag_hypothesis = 23.0

# the hypothesis states the weight per bag, which can be calculated from the premise
# calculate the weight per bag in the premise
oranges_per_bag_premise = total_oranges_premise / total_bags_premise
if oranges_per_bag_hypothesis != oranges_per_bag_premise:
    # check if the weight per bag in the hypothesis contradicts the calculated weight per bag from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

