class_size_premise = 700
class_size_hypothesis = 200
grade_diff_premise = 24
grade_diff_hypothesis = 24

# the hypothesis refers to the number of students and grades mentioned in the premise
if class_size_hypothesis <= class_size_premise:
    # check if the estimate of 'class_size_hypothesis' contradicts the number of students in the premise
    label = "contradiction"
elif grade_diff_hypothesis!= grade_diff_premise:
    # check if the number of grades higher in the hypothesis contradicts the number of grades higher reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
