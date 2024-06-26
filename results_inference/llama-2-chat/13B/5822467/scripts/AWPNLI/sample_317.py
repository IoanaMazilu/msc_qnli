# compute the total number of students in the premise
total_students_premise = students_premise * classrooms_premise

# compute the total number of students in the hypothesis
total_students_hypothesis = students_hypothesis * classrooms_hypothesis

# compare the total number of students in the premise and hypothesis
if total_students_hypothesis > total_students_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif total_students_hypothesis < total_students_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise are neutral
    label = "neutral"

print(label)
