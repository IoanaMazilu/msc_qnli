# Premise: In another class of 200 students there were 24 grades higher than Lena’s.
# Hypothesis: In another class of less than 700 students there were 24 grades higher than Lena’s.
# Golden Label: entailment

students_premise = 200
students_hypothesis = 700
grades_higher_than_lena_premise = 24
grades_higher_than_lena_hypothesis = 24

# the hypothesis refers to the number of students and grades mentioned in the premise
if students_hypothesis < students_premise:
    # check if the 'students_hypothesis' contradicts the number of students in the premise
    label = "contradiction"
elif grades_higher_than_lena_hypothesis != grades_higher_than_lena_premise:
    # check if the number of grades in the hypothesis contradicts the number of grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

