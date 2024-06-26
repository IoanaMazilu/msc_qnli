clothing_to_wash_premise = 47.0
clothing_in_first_load_premise = 17.0
remaining_clothing_premise = clothing_to_wash_premise - clothing_in_first_load_premise
small_loads_hypothesis = 5.0
clothing_per_small_load_hypothesis = 10.0

# the hypothesis refers to the number of pieces of clothing that could go in each small load, which is also mentioned in the premise
# compute the number of pieces of clothing that could go in each small load in the premise
clothing_per_small_load_premise = remaining_clothing_premise / small_loads_hypothesis
if clothing_per_small_load_hypothesis!= clothing_per_small_load_premise:
    # check if the number of pieces of clothing per small load in the hypothesis contradicts the number of pieces of clothing per small load from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)