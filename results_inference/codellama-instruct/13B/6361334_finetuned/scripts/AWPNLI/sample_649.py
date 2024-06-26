oranges_premise = 45.0
bags_premise = 23.0
oranges_hypothesis = 1.4

# the hypothesis refers to the number of bags, which are also mentioned in the premise
# compute the total number of oranges in the premise
total_oranges_premise = oranges_premise / bags_premise
if total_oranges_hypothesis!= total_oranges_premise:
    # check if the number of oranges in the hypothesis contradicts the number of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
