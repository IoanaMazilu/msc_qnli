centrifuges_premise = 54000
reactor_power_premise = 1000

# the hypothesis talks about the number of centrifuges needed to fuel a 1000 MW reactor, which is also mentioned in the premise
if centrifuges_premise == reactor_power_premise:
    # the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # the number of centrifuges in the hypothesis does not contradict the number of centrifuges in the premise, but the power of the reactor does
    label = "neutral"

print(label)
