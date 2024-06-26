students_premise = 200
students_hypothesis = 300
grades_higher_premise = 24
grades_higher_hypothesis = 24

# the hypothesis talks about the number of students and the number of grades higher than Lena's, referenced also in the premise
if students_hypothesis!= students_premise:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
elif grades_higher_hypothesis!= grades_higher_premise:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
