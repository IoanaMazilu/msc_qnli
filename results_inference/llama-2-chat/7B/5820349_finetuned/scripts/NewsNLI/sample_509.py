explosive_devices_premise = 2
explosive_devices_hypothesis = 2

# the hypothesis mentions the number of explosive devices found in trees, which is also mentioned in the premise
if explosive_devices_hypothesis!= explosive_devices_premise:
    # check if the number of explosive devices in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of explosive devices in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
