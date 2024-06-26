students_premise = 10.0
students_left_premise = 4.0
students_new_premise = 42.0
students_hypothesis = 50.0

# compare the number of students in the premise and hypothesis
if students_hypothesis == students_premise + students_left_premise:
    # if the number of students in the hypothesis is equal to the sum of the number of students in the premise and those who left, we can infer entailment
    label = "entailment"
elif students_hypothesis!= students_premise + students_left_premise:
    # if the number of students in the hypothesis contradicts the sum of the number of students in the premise and those who left, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
