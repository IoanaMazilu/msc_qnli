total_students_premise = 390.0
classroom_capacity_premise = 30.0
classrooms_hypothesis = 11.0

# the hypothesis refers to the number of classrooms, which is also mentioned in the premise
# compute the number of classrooms needed from the premise
classrooms_premise = total_students_premise / classroom_capacity_premise
if classrooms_hypothesis!= classrooms_premise:
    # check if the number of classrooms from the hypothesis contradicts the number of classrooms from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
