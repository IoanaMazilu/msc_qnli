# define variables for the measurements in the premise and hypothesis
carton_length_premise = 25
carton_length_hypothesis = 15
carton_width_premise = 42
carton_width_hypothesis = 42
carton_height_premise = 60
carton_height_hypothesis = 60

# the hypothesis gives exact measures for the carton's dimensions
# we must compare if these measures contradict the ones from the premise
if carton_length_premise != carton_length_hypothesis:
    label = "contradiction"
elif carton_width_premise != carton_width_hypothesis:
    label = "contradiction"
elif carton_height_premise != carton_height_hypothesis:
    label = "contradiction"
else:
    # if all measures from the hypothesis match the ones from the premise, we can infer entailment
    label = "entailment"

print(label)
