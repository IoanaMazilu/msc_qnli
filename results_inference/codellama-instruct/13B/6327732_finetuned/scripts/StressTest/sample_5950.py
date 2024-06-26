T_premise = 20
T_hypothesis = 20
K_premise = 32
K_hypothesis = 32

# the hypothesis refers to the temperature and the Kelvin value, both mentioned in the premise
if T_premise!= T_hypothesis:
    # check if the hypothesis value contradicts the temperature value in the premise
    label = "contradiction"
elif K_premise!= K_hypothesis:
    # check if the hypothesis value contradicts the Kelvin value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
