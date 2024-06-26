components_premise = 60
components_hypothesis = 30
percent_machine_a_premise = 0.8
percent_machine_b_premise = 0.2
percent_machine_a_hypothesis = 0.8
percent_machine_b_hypothesis = 0.2

# the hypothesis refers to the number of components, the efficiency of Machine A and Machine B
if components_premise <= components_hypothesis:
    # check if the estimate of 'components_hypothesis' contradicts the number of components in the premise
    label = "contradiction"
elif percent_machine_a_premise!= percent_machine_a_hypothesis or percent_machine_b_premise!= percent_machine_b_hypothesis:
    # check if the efficiency of Machine A or Machine B in the hypothesis contradicts the efficiency reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
