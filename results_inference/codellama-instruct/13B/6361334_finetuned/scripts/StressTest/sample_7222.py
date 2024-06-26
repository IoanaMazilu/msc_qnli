students_premise = 700
students_hypothesis = 200
grades_higher_premise = 24
grades_higher_hypothesis = 24

# the hypothesis refers to the number of students and grades higher than Lena's mentioned in the premise
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of less than'students_premise'
    label = "contradiction"
elif grades_higher_hypothesis!= grades_higher_premise:
    # check if the number of grades higher in the hypothesis contradicts the number of grades higher reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
