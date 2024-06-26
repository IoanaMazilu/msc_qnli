hamburgers_made_premise = 9.0
hamburgers_served_premise = 3.0
hamburgers_left_over_hypothesis = 6.0

# the hypothesis refers to the number of hamburgers left over, which can be computed from the premise
# compute the number of hamburgers left over in the premise
hamburgers_left_over_premise = hamburgers_made_premise - hamburgers_served_premise
if hamburgers_left_over_hypothesis!= hamburgers_left_over_premise:
    # check if the number of hamburgers left over in the hypothesis contradicts the number of hamburgers left over from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
