required_marks_ratio_premise = 0.5
required_marks_ratio_hypothesis = 0.4
marks_obtained = 50
failed_by_marks = 10

# the hypothesis refers to the same information about Paul's marks as the premise
if required_marks_ratio_hypothesis >= required_marks_ratio_premise:
    # check if the 'required_marks_ratio_hypothesis' contradicts the required percentage in the premise
    label = "contradiction"
elif marks_obtained != 50 or failed_by_marks != 10:
    # check if the marks obtained or the marks he failed by in the hypothesis contradicts the same information in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
