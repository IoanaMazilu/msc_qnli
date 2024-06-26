watts_premise = 150
watts_hypothesis = 150

# the hypothesis mentions the minimum wattage for the lighting, which is also mentioned in the premise
if watts_hypothesis != watts_premise:
    # check if the wattage in the hypothesis contradicts the wattage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
