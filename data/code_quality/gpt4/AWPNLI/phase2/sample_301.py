total_clothing_premise = 47.0
first_load_premise = 17.0
loads_premise = 5.0
load_clothing_hypothesis = 10.0

# the hypothesis refers to the number of clothes per load which can be calculated from the premise
# calculate the number of clothes left for the small loads in the premise
remaining_clothing_premise = total_clothing_premise - first_load_premise

# calculate how many clothes go into each of the small loads
clothes_per_load_premise = remaining_clothing_premise / loads_premise

if clothes_per_load_premise != load_clothing_hypothesis:
    # check if the number of clothes per load in the hypothesis contradicts the calculated number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
