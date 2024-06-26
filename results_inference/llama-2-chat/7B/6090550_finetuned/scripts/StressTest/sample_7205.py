 marks_reema_premise = 85
marks_reema_hypothesis = 70

# the hypothesis talks about the marks secured by Reema, which is also referenced in the premise
if marks_reema_hypothesis!= marks_reema_premise:
    # check if the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
