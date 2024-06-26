class_size_premise = 200
class_size_hypothesis = 300
grades_higher_premise = 24
grades_higher_hypothesis = 24

# the hypothesis refers to the number of grades higher than Lena's mentioned in the premise
if class_size_premise!= class_size_hypothesis:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
elif grades_higher_hypothesis!= grades_higher_premise:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of grades higher than Lena's reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
