total_components_premise = 60
total_components_hypothesis = 30
machine_A_premise = 0.8 * total_components_premise
machine_B_premise = 0.2 * total_components_premise
machine_A_hypothesis = 0.8 * total_components_hypothesis
machine_B_hypothesis = 0.2 * total_components_hypothesis

# the hypothesis talks about the total electronic components and how they are distributed between machines A and B
if total_components_hypothesis >= total_components_premise:
    # check if the number of total components in the hypothesis contradicts the number of total components in the premise
    label = "contradiction"
elif machine_A_premise != machine_A_hypothesis or machine_B_premise != machine_B_hypothesis:
    # check if the distribution of components between machines A and B in the hypothesis contradicts the distribution in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of components
    # any number of components greater than 'total_components_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
