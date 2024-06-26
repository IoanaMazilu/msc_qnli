grade_premise = 80
grade_hypothesis = 80
class_size_premise = 120
class_size_hypothesis = 120

# the hypothesis refers to the grade and class size mentioned in the premise
if grade_hypothesis <= grade_premise:
    # check if the estimate of 'grade_hypothesis' contradicts the grade in the premise
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
