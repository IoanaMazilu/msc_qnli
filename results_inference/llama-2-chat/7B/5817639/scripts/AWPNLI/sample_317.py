students_premise = 390.0
students_per_classroom = 30.0
classrooms_hypothesis = 11.0

# compute the total number of classrooms needed based on the premise
total_classrooms_premise = students_premise / students_per_classroom

# check if the number of classrooms in the hypothesis contradicts the estimate from the premise
if total_classrooms_hypothesis!= total_classrooms_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
