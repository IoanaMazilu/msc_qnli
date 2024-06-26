premise_pounds_oranges = 45.0
premise_bags_oranges = 23.0
hypothesis_bags_oranges = 1.95652173913

# the hypothesis refers to the number of bags, which are also mentioned in the premise
# compute the total number of pounds of oranges in the premise
total_pounds_oranges_premise = premise_pounds_oranges / premise_bags_oranges
if total_pounds_oranges_premise!= hypothesis_bags_oranges:
    # check if the number of bags in the hypothesis contradicts the number of pounds of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
