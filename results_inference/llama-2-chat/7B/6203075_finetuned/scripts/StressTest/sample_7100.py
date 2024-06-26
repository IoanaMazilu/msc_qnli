average_marks_premise = 36
average_marks_hypothesis = 36

# the hypothesis refers to the marks secured by Reema, which is also mentioned in the premise
if average_marks_hypothesis <= average_marks_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it is a contradiction
    label = "contradiction"

print(label)
