random_processing_students_premise = 310
random_processing_students_hypothesis = 110
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_subjects_students_premise = 112
both_subjects_students_hypothesis = 112

# the hypothesis refers to the number of students enrolled in different subjects mentioned in the premise
if random_processing_students_hypothesis > random_processing_students_premise:
    # check if the estimate of 'random_processing_students_hypothesis' contradicts the number of students enrolled in random processing methods in the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students enrolled in Scramjet rocket engines in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
elif both_subjects_students_hypothesis!= both_subjects_students_premise:
    # check if the number of students enrolled in both subjects in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
