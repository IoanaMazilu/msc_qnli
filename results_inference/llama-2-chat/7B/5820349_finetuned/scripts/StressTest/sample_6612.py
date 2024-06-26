random_processing_students_premise = 312
random_processing_students_hypothesis = 112
scramjet_students_premise = 234
scramjet_students_hypothesis = 234
both_subjects_students_premise = 112
both_subjects_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects mentioned in the premise
if random_processing_students_premise <= random_processing_students_hypothesis:
    # check if the estimate of 'random_processing_students_hypothesis' contradicts the number of random-processing methods students in the premise
    label = "contradiction"
elif scramjet_students_premise!= scramjet_students_hypothesis:
    # check if the number of Scramjet rocket engines students in the hypothesis contradicts the number of Scramjet rocket engines students reported in the premise
    label = "contradiction"
elif both_subjects_students_premise!= both_subjects_students_hypothesis:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students studying both subjects reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
