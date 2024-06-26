injured_premise = 2
critical_premise = "critical"
hospitalized_premise = "out-of-area"

injured_hypothesis = 2
critical_hypothesis = "critical"

# the hypothesis mentions the number of injured people and their critical condition, which are also mentioned in the premise
# however, the hypothesis does not provide any new information that can entail or contradict the premise
label = "neutral"

print(label)
