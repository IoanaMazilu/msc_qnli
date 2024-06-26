clothes_premise = 47.0
clothes_per_load_premise = 17.0
total_loads_premise = 5.0
clothes_per_load_hypothesis = 10.0

# the hypothesis refers to the number of clothes per load, which is also mentioned in the premise
# compute the total number of clothes per load in the premise
clothes_per_load_premise = clothes_per_load_premise
if clothes_per_load_hypothesis!= clothes_per_load_premise:
    # check if the number of clothes per load from the hypothesis contradicts the number of clothes per load from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
