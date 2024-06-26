reema_marks_premise = 36
reema_marks_written = 66
reema_marks_hypothesis = 36

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if reema_marks_hypothesis > reema_marks_premise:
    # check if the hypothesis value contradicts the specific number of 'reema_marks_premise'
    label = "contradiction"
elif reema_marks_hypothesis != reema_marks_written:
    # check if the number of marks written for Reema in the hypothesis contradicts the number of marks written for Reema reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
