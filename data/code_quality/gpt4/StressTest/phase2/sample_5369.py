boy_students_premise = 80
boy_students_hypothesis = 80
girl_students_premise = 75
girl_students_hypothesis = 75

# the hypothesis refers to the percentage of boy and girl students mentioned in the premise
if boy_students_hypothesis > boy_students_premise:
    # check if the estimate of 'boy_students_hypothesis' contradicts the percentage of boy students in the premise
    label = "contradiction"
elif girl_students_hypothesis != girl_students_premise:
    # check if the percentage of girl students in the hypothesis contradicts the percentage of girl students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
