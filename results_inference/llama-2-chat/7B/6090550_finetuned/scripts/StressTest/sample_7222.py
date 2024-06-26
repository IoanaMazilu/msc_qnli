 class_size_premise = 700
class_size_hypothesis = 200
grade_higher_premise = 24
grade_higher_hypothesis = 24

# the hypothesis refers to the class size and the number of grades higher than Lena's
if class_size_hypothesis <= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size in the premise
    label = "contradiction"
elif grade_higher_hypothesis!= grade_higher_premise:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of grades higher than Lena's in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
