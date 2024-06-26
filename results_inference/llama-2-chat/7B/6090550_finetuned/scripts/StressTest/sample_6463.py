random_processing_students_premise = 102
random_processing_students_hypothesis = 302
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
joint_students_premise = 112
joint_students_hypothesis = 112

# the hypothesis talks about the number of students studying random-processing methods, scramjet rocket engines, and both
if random_processing_students_hypothesis <= random_processing_students_premise:
    # check if the number of students studying random-processing methods in the hypothesis contradicts the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying scramjet rocket engines in the hypothesis contradicts the premise
    label = "contradiction"
elif joint_students_hypothesis!= joint_students_premise:
    # check if the number of students studying both in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
