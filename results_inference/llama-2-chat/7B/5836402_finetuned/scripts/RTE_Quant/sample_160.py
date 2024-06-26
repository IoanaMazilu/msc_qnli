centrifuges_premise = 54000
centrifuges_hypothesis = 54000
reactor_power_premise = 1000
reactor_power_hypothesis = 1000

# the hypothesis and premise mention the same number of centrifuges and the same power of the reactor
# however, the hypothesis does not specify the reactor being built by Russia, which is mentioned in the premise
# the hypothesis does not contradict the premise, but it does not provide additional information that can be used to infer entailment
label = "neutral"

print(label)
