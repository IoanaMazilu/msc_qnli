birds_speed_premise = 4
birds_speed_hypothesis_west = 7
birds_speed_hypothesis_east = 1

# the hypothesis refers to the speed of the two birds mentioned in the premise
if birds_speed_hypothesis_west <= birds_speed_premise:
    # check if the estimate of 'birds_speed_hypothesis_west' contradicts the speed of the first bird in the premise
    label = "contradiction"
elif birds_speed_hypothesis_east!= 1:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
