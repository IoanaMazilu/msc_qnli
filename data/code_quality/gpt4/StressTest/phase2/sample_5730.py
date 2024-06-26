marks_premise = 46
correct_marks_premise = 96
marks_hypothesis = 76
correct_marks_hypothesis = 96

# the hypothesis refers to Reema's marks mentioned in the premise
if marks_hypothesis < marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif correct_marks_hypothesis != correct_marks_premise:
    # check if the correct marks in the hypothesis contradicts the correct marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
