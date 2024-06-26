reema_marks_premise = 45
reema_marks_hypothesis = 35

# the hypothesis talks about a scenario where Reema's marks were written as a certain number, which is also referenced in the premise
if reema_marks_hypothesis != reema_marks_premise:
    # check if the hypothetical marks in the hypothesis contradicts the hypothetical marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothetical marks in the hypothesis do not contradict the hypothetical marks in the premise, we can infer entailment
    label = "entailment"

print(label)
