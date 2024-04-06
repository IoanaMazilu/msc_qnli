# Premise: '' Experts determined that the two explosive devices were planted in one of the trees in the area,'' the ministry said, adding that an investigation was under way.
# Hypothesis: It says that two explosive devices were in trees in the area.
# Golden Label: neutral

explosive_devices_premise = 2
explosive_devices_hypothesis = 2

# the hypothesis mentions the number of explosive devices in trees in the area, which is also mentioned in the premise
if explosive_devices_hypothesis != explosive_devices_premise:
    # check if the number of explosive devices in the hypothesis contradicts the number of explosive devices reported in the premise
    label = "contradiction"
else:
    # if the number of explosive devices in the hypothesis does not contradict the number of explosive devices in the premise, we can infer entailment
    label = "entailment"

print(label)

