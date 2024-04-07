# Premise: 50% of students from 200 Science students are locals and 85% of total 120 Commerce students are locals.
# Hypothesis: more than 50% of students from 200 Science students are locals and 85% of total 120 Commerce students are locals.
# Golden Label: contradiction

science_students_premise_percentage = 50
science_students_premise_total = 200
commerce_students_premise_percentage = 85
commerce_students_premise_total = 120

science_students_hypothesis_percentage = 50
commerce_students_hypothesis_percentage = 85

# the hypothesis refers to the percentage of local students in science and commerce, mentioned in the premise
if science_students_hypothesis_percentage <= science_students_premise_percentage and commerce_students_hypothesis_percentage == commerce_students_premise_percentage:
    # check if the estimate of 'science_students_hypothesis_percentage' contradicts the percentage of science students in the premise
    # and if the percentage of commerce students is the same in both the premise and the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

