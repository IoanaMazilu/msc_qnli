classes_johnny_premise = 4
classes_johnny_hypothesis = 1

# the hypothesis talks about the number of classes Johnny has, also referenced in the premise
if classes_johnny_premise <= classes_johnny_hypothesis:
    # check if the number of classes in the premise contradicts the hypothesis estimate of more than 'classes_johnny_hypothesis'
    label = "contradiction"
else:
    # if the number of classes in the premise does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
