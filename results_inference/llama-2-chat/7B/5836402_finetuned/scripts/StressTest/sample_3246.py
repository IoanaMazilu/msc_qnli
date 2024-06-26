represented_students_premise = 90
represented_students_hypothesis = 50
percentage_premise = 100
percentage_hypothesis = 100

# the hypothesis refers to the number of represented students and the percentage at the school, which are also mentioned in the premise
if represented_students_hypothesis >= represented_students_premise:
    # check if the hypothesis value contradicts the estimate of'represented_students_premise'
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
