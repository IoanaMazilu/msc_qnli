random_processing_students_premise = 312
scramjet_students_premise = 234
common_students_premise = 112

random_processing_students_hypothesis = 112
scramjet_students_hypothesis = 234
common_students_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, scramjet rocket engines, and both
if random_processing_students_hypothesis < random_processing_students_premise:
    # check if the estimate of 'random_processing_students_hypothesis' contradicts the number of students studying random-processing methods in the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying scramjet rocket engines in the hypothesis contradicts the number of students studying scramjet rocket engines in the premise
    label = "contradiction"
elif common_students_hypothesis!= common_students_premise:
    # check if the number of students studying both in the hypothesis contradicts the number of students studying both in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
