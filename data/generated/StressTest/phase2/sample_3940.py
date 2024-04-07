# Premise: less than 500 students took a mock exam in Delhi, 60% of the boys and 80% of the girls cleared the cut off in the examination.
# Hypothesis: 400 students took a mock exam in Delhi, 60% of the boys and 80% of the girls cleared the cut off in the examination.
# Golden Label: neutral

students_exam_premise = 500
students_exam_hypothesis = 400
boys_passed_premise = 0.6
boys_passed_hypothesis = 0.6
girls_passed_premise = 0.8
girls_passed_hypothesis = 0.8

# the hypothesis refers to the number of students who took the exam and the percentage of boys and girls who passed, all mentioned in the premise
if students_exam_hypothesis >= students_exam_premise:
    # check if the number of students in the hypothesis contradicts the estimate of less than 'students_exam_premise'
    label = "contradiction"
elif boys_passed_hypothesis != boys_passed_premise or girls_passed_hypothesis != girls_passed_premise:
    # check if the percentage of boys and girls who passed in the hypothesis contradicts the percentage given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

