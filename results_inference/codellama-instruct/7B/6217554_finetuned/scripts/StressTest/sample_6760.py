marks_premise = 56
marks_hypothesis = 46

# the hypothesis talks about the marks secured by Reema, referenced also in the premise
if marks_hypothesis >= marks_premise:
    # check if the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
