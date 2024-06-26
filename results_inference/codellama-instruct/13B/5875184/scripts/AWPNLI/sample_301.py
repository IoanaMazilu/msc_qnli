premise_clothing = 47.0
premise_loads = 1.0
hypothesis_clothing = 10.0
hypothesis_loads = 5.0

# the hypothesis refers to the number of clothing pieces that can go in each load
# compute the total number of clothing pieces in the premise
total_clothing_premise = premise_clothing / premise_loads
if total_clothing_premise!= hypothesis_clothing:
    # check if the number of clothing pieces in the hypothesis contradicts the number of clothing pieces from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
