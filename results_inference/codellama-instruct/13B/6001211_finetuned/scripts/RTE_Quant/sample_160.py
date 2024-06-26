centrifuges_premise = 54000
centrifuges_hypothesis = 54000
reactor_power_premise = 1000
reactor_power_hypothesis = 1000

# the hypothesis talks about the number of centrifuges and the power of a reactor, which are also mentioned in the premise
if centrifuges_hypothesis!= centrifuges_premise:
    # check if the number of centrifuges in the hypothesis contradicts the number of centrifuges from the premise
    label = "contradiction"
elif reactor_power_hypothesis!= reactor_power_premise:
    # check if the reactor power in the hypothesis contradicts the reactor power in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
