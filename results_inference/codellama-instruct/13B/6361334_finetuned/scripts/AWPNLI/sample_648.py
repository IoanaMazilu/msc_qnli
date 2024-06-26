pounds_oranges_premise = 45.0
pounds_oranges_per_bag_premise = 23.0
bags_hypothesis = 1.95652173913

# the hypothesis refers to the number of bags, which are also mentioned in the premise
# compute the total number of pounds of oranges in the premise
total_pounds_oranges_premise = pounds_oranges_premise / pounds_oranges_per_bag_premise
if total_pounds_oranges_premise!= bags_hypothesis:
    # check if the number of bags in the hypothesis contradicts the number of pounds of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
