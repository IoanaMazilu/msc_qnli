initial_marks_premise = 99
initial_marks_hypothesis = 99
corrected_marks_premise = 35
corrected_marks_hypothesis = 75

# the hypothesis refers to the initial marks of Reema mentioned in the premise
if initial_marks_hypothesis!= initial_marks_premise:
    # check if the initial marks in the hypothesis contradicts the initial marks reported in the premise
    label = "contradiction"
elif corrected_marks_hypothesis!= corrected_marks_premise:
    # check if the corrected marks in the hypothesis contradicts the corrected marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
