collected_oranges_premise = 77.0
eaten_oranges_premise = 2.0
total_oranges_hypothesis = 75.0

# the hypothesis refers to the number of oranges, which are also mentioned in the premise
# compute the total number of oranges remained in the premise
total_oranges_premise = collected_oranges_premise - eaten_oranges_premise
if total_oranges_hypothesis != total_oranges_premise:
    # check if the number of oranges in the hypothesis contradicts the number of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
