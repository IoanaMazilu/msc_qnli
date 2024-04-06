# Premise: China is the largest global producer and consumer of coal, comprising 75 percent of China's total energy consumption.
# Hypothesis: Coal makes up 75 percent of China's energy use.
# Golden Label: entailment

coal_consumption_premise = 0.75
coal_consumption_hypothesis = 0.75

# the hypothesis mentions the percentage of coal in China's energy use, which is also mentioned in the premise
if coal_consumption_hypothesis != coal_consumption_premise:
    # check if the coal consumption percentage in the hypothesis contradicts that in the premise
    label = "contradiction"
else:
    # if the coal consumption percentage in the hypothesis does not contradict that in the premise, we can infer entailment
    label = "entailment"

print(label)

