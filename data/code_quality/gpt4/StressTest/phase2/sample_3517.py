science_students_premise = 100 * 0.85
science_students_hypothesis = 100 * 0.25
commerce_students_premise = 120 * 0.85
commerce_students_hypothesis = 120 * 0.85

# the hypothesis refers to the percentage of local students in Science and Commerce mentioned in the premise
if science_students_hypothesis >= science_students_premise:
    # check if the percentage of 'science_students_hypothesis' contradicts the percentage of science students in the premise
    label = "contradiction"
elif commerce_students_hypothesis != commerce_students_premise:
    # check if the percentage of commerce students in the hypothesis contradicts the percentage of commerce students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and percentages do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
