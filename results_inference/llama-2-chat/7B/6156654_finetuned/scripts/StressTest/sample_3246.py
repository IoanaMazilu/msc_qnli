students_premise = 90
students_hypothesis = 50
percentage_premise = 0 # percentage is not mentioned in the hypothesis
percentage_hypothesis = 0 # percentage is not mentioned in the hypothesis

# the hypothesis refers to the number of students and the percentage of boys, both mentioned in the premise
if students_premise >= students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif percentage_premise!= percentage_hypothesis:
    # check if the percentage of boys in the hypothesis contradicts the percentage of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
