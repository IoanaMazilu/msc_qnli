centrifuges_premise = 54000
centrifuges_hypothesis = 54000
reactor_megawatts_premise = 1000
reactor_megawatts_hypothesis = 1000

# the hypothesis mentions the number of centrifuges and the power of the reactor, which are also mentioned in the premise
if centrifuges_hypothesis!= centrifuges_premise:
    # check if the number of centrifuges in the hypothesis contradicts the number of centrifuges in the premise
    label = "contradiction"
elif reactor_megawatts_hypothesis!= reactor_megawatts_premise:
    # check if the power of the reactor in the hypothesis contradicts the power of the reactor in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
