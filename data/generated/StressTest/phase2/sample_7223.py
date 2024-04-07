# Premise: In another class of 200 students there were 24 grades higher than Lena’s.
# Hypothesis: In another class of 300 students there were 24 grades higher than Lena’s.
# Golden Label: contradiction

students_class_premise = 200
grades_higher_than_lena_premise = 24

students_class_hypothesis = 300
grades_higher_than_lena_hypothesis = 24

# the hypothesis talks about the number of students in a class and the number of grades higher than Lena's, both referenced in the premise
if students_class_hypothesis != students_class_premise:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
elif grades_higher_than_lena_hypothesis != grades_higher_than_lena_premise:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of grades higher than Lena's reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

