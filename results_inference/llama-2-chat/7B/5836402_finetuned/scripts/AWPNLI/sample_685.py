bottles_water_premise = 45.0
drunk_bottles_premise = 14.0
drunk_by_sister_premise = 8.0
left_bottles_hypothesis = 18.0

# the hypothesis refers to the number of bottles, which are also mentioned in the premise
# compute the total number of bottles left in the premise
total_bottles_premise = bottles_water_premise - drunk_bottles_premise - drunk_by_sister_premise
if left_bottles_hypothesis!= total_bottles_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
