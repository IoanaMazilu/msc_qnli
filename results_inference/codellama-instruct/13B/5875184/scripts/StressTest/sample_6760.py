marks_reema_premise = 56
marks_reema_hypothesis = 46

# the hypothesis refers to the number of marks secured by Reema, which is mentioned in the premise
if marks_reema_premise <= marks_reema_hypothesis:
    # check if the estimate of'marks_reema_hypothesis' contradicts the number of marks secured by Reema in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks secured by Reema
    # any number of marks greater than'marks_reema_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
