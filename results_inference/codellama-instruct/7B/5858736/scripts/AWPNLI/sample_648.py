premise_oranges_total = 45.0
premise_oranges_per_bag = 23.0
hypothesis_bags = 1.95652173913

# the hypothesis refers to the number of bags, which is also mentioned in the premise
# compute the total number of oranges in the premise
total_oranges_premise = premise_oranges_total / premise_oranges_per_bag
if total_oranges_hypothesis!= total_oranges_premise:
    # check if the number of oranges in the hypothesis contradicts the number of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
