total_clothing_premise = 47.0
washed_clothing_premise = 17.0
loads_premise = 5.0

# the hypothesis refers to the number of clothes in each load, which are not mentioned in the premise
# compute the total number of clothes in each load from the premise
clothes_per_load_premise = total_clothing_premise / loads_premise
if clothes_per_load_hypothesis!= clothes_per_load_premise:
    # check if the number of clothes per load from the hypothesis contradicts the number of clothes per load from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
