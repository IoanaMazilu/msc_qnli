epicenter_premise = "Negros"
epicenter_hypothesis = "Negros"
distance_premise = 360
distance_hypothesis = 360

# the hypothesis mentions the epicenter of the quake, which is also mentioned in the premise
# however, the hypothesis does not provide any additional information about the distance from Manila
# therefore, we cannot infer entailment or contradiction
label = "neutral"

print(label)
