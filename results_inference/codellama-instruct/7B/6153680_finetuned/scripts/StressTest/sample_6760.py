marks_secured_premise = 56
marks_secured_hypothesis = 46

# the hypothesis talks about the marks secured by Reema, which is also mentioned in the premise
if marks_secured_hypothesis >= marks_secured_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
