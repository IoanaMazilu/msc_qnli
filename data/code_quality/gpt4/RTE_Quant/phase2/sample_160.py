centrifuge_premise = 54000
centrifuge_hypothesis = 54000
reactor_premise = 1000
reactor_hypothesis = 1000

# the hypothesis talks about the number of centrifuges and the capacity of the reactor
# which is the same information provided in the premise
if centrifuge_hypothesis != centrifuge_premise:
    # check if the number of centrifuges in the hypothesis contradicts the number of centrifuges in the premise
    label = "contradiction"
elif reactor_hypothesis != reactor_premise:
    # check if the reactor capacity in the hypothesis contradicts the reactor capacity in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
