class_size_premise = 200
grades_higher_premise = 24

class_size_hypothesis = 300
grades_higher_hypothesis = 24

# the hypothesis refers to the class size and number of grades higher mentioned in the premise
if class_size_hypothesis <= class_size_premise:
    # check if the estimate of 'class_size_hypothesis' contradicts the class size reported in the premise
    label = "contradiction"
elif grades_higher_hypothesis!= grades_higher_premise:
    # check if the number of grades higher in the hypothesis contradicts the number of grades higher reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
