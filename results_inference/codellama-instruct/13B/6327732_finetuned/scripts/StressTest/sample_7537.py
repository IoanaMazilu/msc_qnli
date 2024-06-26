subjects_premise = 5
subjects_hypothesis = 5
marks_premise = [40, 60, 70, 80, 80]
marks_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the marks obtained in different subjects, mentioned in the premise
if subjects_premise!= subjects_hypothesis:
    # check if the number of subjects in the hypothesis contradicts the number of subjects mentioned in the premise
    label = "contradiction"
elif marks_hypothesis!= marks_premise:
    # check if the marks obtained in the hypothesis contradicts the marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
