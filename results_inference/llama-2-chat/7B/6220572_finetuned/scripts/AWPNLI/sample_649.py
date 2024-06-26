pounds_oranges_premise = 45.0
bags_hypothesis = 1.4

# the hypothesis refers to the number of bags, which is also mentioned in the premise
# compute the number of bags from the premise
bags_premise = pound_oranges_premise / pound_oranges_per_bag
if bags_hypothesis!= bags_premise:
    # check if the number of bags from the hypothesis contradicts the number of bags from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
