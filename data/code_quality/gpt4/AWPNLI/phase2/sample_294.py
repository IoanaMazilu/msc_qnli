washing_capacity_premise = 8.0
shirts_premise = 39.0
sweaters_premise = 33.0
loads_hypothesis = 9.0

# the hypothesis refers to the number of loads, which is indirectly mentioned in the premise
# compute the total number of clothes and then calculate the total number of loads needed according to the washing capacity
total_clothes_premise = shirts_premise + sweaters_premise
total_loads_premise = total_clothes_premise / washing_capacity_premise

if loads_hypothesis != round(total_loads_premise):
    # check if the number of loads in the hypothesis contradicts the calculated number of loads from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
