components_premise = 30
components_hypothesis = 60
percent_machine_A_premise = 0.8
percent_machine_B_premise = 0.2
percent_machine_A_hypothesis = 0.8
percent_machine_B_hypothesis = 0.2

# the hypothesis talks about the total number of components, the percentage of components efficiently manufactured by Machine A and Machine B
# all these quantities are also mentioned in the premise
if components_hypothesis <= components_premise:
    # check if the total number of components in the hypothesis contradicts the estimate of more than 'components_premise'
    label = "contradiction"
elif percent_machine_A_hypothesis!= percent_machine_A_premise or percent_machine_B_hypothesis!= percent_machine_B_premise:
    # check if the percentage of components efficiently manufactured by Machine A and Machine B in the hypothesis contradicts the percentages reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of components
    # any total number of components greater than 'components_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
