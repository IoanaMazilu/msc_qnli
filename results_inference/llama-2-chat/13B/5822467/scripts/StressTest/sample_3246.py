percentage_premise = 90
percentage_hypothesis = 50
students_premise = x

# the hypothesis refers to the percentage of boys at Jones Elementary School
if percentage_hypothesis <= percentage_premise:
    # check if the hypothesis value contradicts the estimate of 'percentage_premise'
    label = "contradiction"
elif students_premise!= x:
    # check if the number of students in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
