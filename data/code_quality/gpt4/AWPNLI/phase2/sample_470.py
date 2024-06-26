hamburgers_initial_premise = 9.0
hamburgers_additional_premise = 3.0
hamburgers_hypothesis = 12.0

# the hypothesis refers to the number of hamburgers, which are also mentioned in the premise
# compute the total number of hamburgers in the premise
total_hamburgers_premise = hamburgers_initial_premise + hamburgers_additional_premise

if hamburgers_hypothesis != total_hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
