 Rahul_position_premise = 62
 Rahul_position_hypothesis = 12
 boys_to_add_premise = 28

# the hypothesis refers to the position of Rahul in a line of boys, mentioned in the premise
if Rahul_position_hypothesis >= Rahul_position_premise:
    # check if the estimate of 'Rahul_position_hypothesis' contradicts the position of Rahul in the premise
    label = "contradiction"
elif boys_to_add_premise!= (28 - Rahul_position_premise):
    # check if the number of boys to be added in the hypothesis contradicts the number of boys to be added reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
