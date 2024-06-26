students_grade_premise = 20
students_grade_hypothesis = 50

# define variables for the numerical entities in the premise and hypothesis
students_lower_grades_premise = students_grade_premise * 0.2
students_lower_grades_hypothesis = students_grade_hypothesis * 0.2

# compare the variables to determine the label
if students_lower_grades_hypothesis > students_lower_grades_premise:
    # the hypothesis implies more students in the lower grades than the premise, so contradiction
    label = "contradiction"
elif students_lower_grades_hypothesis == students_lower_grades_premise:
    # the hypothesis and premise are equal, so neutral
    label = "neutral"
else:
    # the hypothesis implies fewer students in the lower grades than the premise, so entailment
    label = "entailment"

print(label)
