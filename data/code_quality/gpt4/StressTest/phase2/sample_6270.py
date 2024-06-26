participants_premise = 7
participants_hypothesis = 8

# the hypothesis refers to the same participants mentioned in the premise
if participants_premise >= participants_hypothesis:
    # check if the number of participants in the premise contradicts the maximum number of participants in the hypothesis
    label = "contradiction"
elif participants_premise != participants_hypothesis - 1:
    # the premise gives the exact number of participants, so if the hypothesis provides an estimate that is not equal to 'participants_premise' + 1, we have a contradiction
    label = "contradiction"
else:
    # if the number of participants in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
