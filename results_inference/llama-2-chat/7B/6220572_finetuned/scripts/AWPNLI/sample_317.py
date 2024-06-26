students_premise = 390.0
classrooms_hypothesis = 11.0

# the hypothesis talks about the number of classrooms, which is also referenced in the premise
# compute the number of classrooms in the premise
classrooms_premise = students_premise / 30.0
if classrooms_hypothesis!= classrooms_premise:
    # check if the number of classrooms in the hypothesis contradicts the number of classrooms from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
