initial_bottles_premise = 14.0
drank_bottles_premise = 8.0
bought_bottles_premise = 45.0
total_bottles_hypothesis = 51.0

# the hypothesis refers to the number of bottles, which are also mentioned in the premise
# compute the total number of bottles in the premise
total_bottles_premise = initial_bottles_premise - drank_bottles_premise + bought_bottles_premise
if total_bottles_hypothesis != total_bottles_premise:
    # check if the number of bottles in the hypothesis contradicts the number of bottles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
