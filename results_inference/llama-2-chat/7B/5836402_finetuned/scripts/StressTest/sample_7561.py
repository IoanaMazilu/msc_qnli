random_processing_students_premise = 110
scramjet_students_premise = 232
shared_students_premise = 112

random_processing_students_hypothesis = 310
scramjet_students_hypothesis = 232
shared_students_hypothesis = 112

# the hypothesis refers to the number of students studying random-processing methods, scramjet rocket engines and both, mentioned in the premise
if random_processing_students_hypothesis!= random_processing_students_premise:
    # check if the number of students studying random-processing methods in the hypothesis contradicts the number of students studying them in the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying scramjet rocket engines in the hypothesis contradicts the number of students studying them in the premise
    label = "contradiction"
elif shared_students_hypothesis!= shared_students_premise:
    # check if the number of students studying both in the hypothesis contradicts the number of students studying both in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
