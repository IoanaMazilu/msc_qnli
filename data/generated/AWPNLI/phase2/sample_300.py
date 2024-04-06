# Premise: Luke had 47.0 pieces of clothing to wash and he put 17.0 of them in 1.0 load, but decided to split the rest into 5.0 equal loads.
# Hypothesis: 6.0 pieces of clothing could go in each of the small loads.
# Golden Label: entailment

total_clothing_premise = 47.0
first_load_premise = 17.0
remaining_loads_premise = 5.0
clothing_per_load_hypothesis = 6.0

# the hypothesis talks about the number of pieces of clothing in each small load, which is also referenced in the premise
# compute the number of pieces of clothing left after the first load
remaining_clothing_premise = total_clothing_premise - first_load_premise
# compute the number of clothing in each of the remaining loads from the premise
clothing_per_load_premise = remaining_clothing_premise / remaining_loads_premise
if clothing_per_load_hypothesis != clothing_per_load_premise:
    # check if the number of pieces of clothing per small load from the hypothesis contradicts the number of pieces of clothing per small load from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

