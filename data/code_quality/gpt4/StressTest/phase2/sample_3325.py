random_processing_students_premise = 412
random_processing_students_hypothesis = 312
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_subjects_students_premise = 114
both_subjects_students_hypothesis = 114

# the hypothesis refers to the number of students studying both subjects, which is also mentioned in the premise
if random_processing_students_hypothesis >= random_processing_students_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the premise
    label = "contradiction"
elif scramjet_students_hypothesis != scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the premise
    label = "contradiction"
elif both_subjects_students_hypothesis != both_subjects_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
