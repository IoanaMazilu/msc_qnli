# Premise: There are 45.0 pounds of oranges and each bag contains 23.0 pounds of oranges.
# Hypothesis: There are 1.4 bags.
# Golden Label: contradiction

oranges_pounds_premise = 45.0
oranges_per_bag_premise = 23.0
bags_hypothesis = 1.4

# the hypothesis refers to the number of bags, which is derived from the number of oranges in pound and the number of oranges in pound per bag from the premise
# compute the number of bags in the premise
bags_premise = oranges_pounds_premise / oranges_per_bag_premise
if bags_hypothesis != bags_premise:
    # check if the number of bags in the hypothesis contradicts the number of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

