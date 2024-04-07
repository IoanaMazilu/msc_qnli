# Premise: 25% of students from 100 Science students are locals and 85% of total 120 Commerce students are locals.
# Hypothesis: less than 85% of students from 100 Science students are locals and 85% of total 120 Commerce students are locals.
# Golden Label: entailment

science_students_premise = 100
science_students_local_premise = 25
commerce_students_premise = 120
commerce_students_local_premise = 85

science_students_hypothesis = 100
science_students_local_hypothesis = 85
commerce_students_hypothesis = 120
commerce_students_local_hypothesis = 85

# the hypothesis refers to the percentages of Science and Commerce local students mentioned in the premise
if science_students_premise != science_students_hypothesis or commerce_students_premise != commerce_students_hypothesis:
    # check if the total number of Science or Commerce students in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif science_students_local_hypothesis <= science_students_local_premise:
    # check if the percentage of local Science students in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif commerce_students_local_hypothesis != commerce_students_local_premise:
    # check if the percentage of local Commerce students in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and percentages do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

