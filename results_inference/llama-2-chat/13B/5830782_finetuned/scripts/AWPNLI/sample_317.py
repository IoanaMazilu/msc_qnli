students_premise = 390.0
students_per_classroom_premise = 30.0
classrooms_hypothesis = 11.0

# the hypothesis refers to the number of classrooms, which can be calculated from the premise
# compute the number of classrooms needed in the premise
classrooms_premise = students_premise / students_per_classroom_premise
if classrooms_hypothesis!= classrooms_premise:
    # check if the number of classrooms in the hypothesis contradicts the number of classrooms from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
