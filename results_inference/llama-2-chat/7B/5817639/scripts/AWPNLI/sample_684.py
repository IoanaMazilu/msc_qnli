bottles_premise = 45.0
drunk_bottles_premise = 14.0
sister_drunk_bottles_premise = 8.0
remaining_bottles_hypothesis = 23.0

# compare the number of bottles left according to the hypothesis and the premise
if remaining_bottles_hypothesis!= (bottles_premise - drunk_bottles_premise - sister_drunk_bottles_premise):
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
