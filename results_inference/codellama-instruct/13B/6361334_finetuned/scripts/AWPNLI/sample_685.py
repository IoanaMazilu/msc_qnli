bottles_premise = 45.0
drunk_premise = 14.0
sister_drunk_premise = 8.0
bottles_hypothesis = 18.0

# the hypothesis refers to the number of bottles left, which are also mentioned in the premise
# compute the total number of bottles in the premise
total_bottles_premise = bottles_premise - drunk_premise - sister_drunk_premise
if total_bottles_hypothesis!= total_bottles_premise:
    # check if the number of bottles in the hypothesis contradicts the number of bottles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
