clothes_to_wash = 47.0
clothes_per_load = 17.0
loads_split = 5.0
clothes_per_small_load = 10.0

# the hypothesis refers to the number of clothes that can go in each small load
if clothes_per_small_load > clothes_per_load:
    # check if the number of clothes per small load contradicts the number of clothes per load in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
