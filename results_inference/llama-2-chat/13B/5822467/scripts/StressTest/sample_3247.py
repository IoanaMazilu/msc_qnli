percentage_premise = 50
percentage_hypothesis = 90
students_premise = 100 - percentage_premise
students_hypothesis = 100 - percentage_hypothesis

# the hypothesis refers to the percentage of boys at Jones Elementary School
if percentage_hypothesis <= percentage_premise:
    # check if the estimate of 'percentage_hypothesis' contradicts the percentage of boys reported in the premise
    label = "contradiction"
elif students_hypothesis!= students_premise:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
