marks_premise = 85
marks_hypothesis = 70

# the hypothesis refers to the marks of Reema mentioned in the premise
if marks_hypothesis!= marks_premise:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis marks do not contradict the premise marks, we can infer entailment
    label = "entailment"

print(label)
