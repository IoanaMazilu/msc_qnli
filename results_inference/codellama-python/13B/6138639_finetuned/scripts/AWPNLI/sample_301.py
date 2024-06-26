total_clothing_premise = 47.0
first_load_premise = 17.0
small_loads_premise = 5.0
total_clothing_hypothesis = 10.0

# the hypothesis refers to the number of pieces of clothing in each small load, which is also mentioned in the premise
# compute the number of pieces of clothing in each small load in the premise
pieces_per_small_load_premise = (total_clothing_premise - first_load_premise) / small_loads_premise
if total_clothing_hypothesis!= pieces_per_small_load_premise:
    # check if the number of pieces of clothing in each small load in the hypothesis contradicts the number of pieces of clothing in each small load from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
