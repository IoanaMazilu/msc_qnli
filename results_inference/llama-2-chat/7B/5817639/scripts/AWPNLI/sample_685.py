bottles_premise = 45.0
drunk_bottles_premise = 14.0
sister_drunk_bottles_premise = 8.0
left_bottles_hypothesis = 23.0

# the hypothesis refers to the number of bottles left, which is also mentioned in the premise
# compute the total number of bottles drunk from the premise
total_drunk_bottles = drunk_bottles_premise + sister_drunk_bottles_premise
if left_bottles_hypothesis!= total_drunk_bottles:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles drunk from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
