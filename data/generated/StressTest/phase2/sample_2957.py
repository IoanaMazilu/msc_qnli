# Premise: 90 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: less than 90 students represent x percent of the boys at Jones Elementary School.
# Golden Label: contradiction

students_premise = 90
students_hypothesis = 90

# the hypothesis refers to the same number of students and the same percentage as the premise
if students_hypothesis < students_premise:
    # check if the number of students in the hypothesis is less than the number of students in the premise
    label = "entailment"
elif students_hypothesis > students_premise:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the number of students in the hypothesis equals the number of students in the premise, we can infer neutrality
    label = "neutral"

print(label)

