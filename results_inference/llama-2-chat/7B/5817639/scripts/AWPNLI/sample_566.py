bus_riders_premise = float(25.0)
bus_riders_hypothesis = float(43.0)

# compare the number of children riding on the bus in the premise and hypothesis
if bus_riders_hypothesis > bus_riders_premise:
    # the number of children riding on the bus in the hypothesis exceeds the number in the premise, so it contradicts
    label = "contradiction"
elif bus_riders_hypothesis < bus_riders_premise:
    # the number of children riding on the bus in the hypothesis is less than the number in the premise, so it entails
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
