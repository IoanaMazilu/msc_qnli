average_marks_premise = 56
average_marks_hypothesis = 46

# the hypothesis talks about the marks secured by Reema, which is also mentioned in the premise
if average_marks_hypothesis >= average_marks_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_marks_hypothesis < average_marks_premise:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutral
    label = "neutral"

print(label)
