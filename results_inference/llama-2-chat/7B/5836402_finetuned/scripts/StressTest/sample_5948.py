don_value_premise = 18
don_value_hypothesis = 18
mass_value_premise = 29
mass_value_hypothesis = 29

# the hypothesis refers to the values of DON and MASS mentioned in the premise
if don_value_hypothesis >= don_value_premise:
    # check if the estimate of 'don_value_hypothesis' contradicts the value of DON in the premise
    label = "contradiction"
elif mass_value_hypothesis!= mass_value_premise:
    # check if the value of MASS in the hypothesis contradicts the value of MASS reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
