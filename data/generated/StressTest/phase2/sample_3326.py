# Premise: At the faculty of Aerospace Engineering, 312 students study Random-processing methods, 232 students study Scramjet rocket engines and 114 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, 212 students study Random-processing methods, 232 students study Scramjet rocket engines and 114 students study them both.
# Golden Label: contradiction

random_processing_students_premise = 312
random_processing_students_hypothesis = 212
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_subjects_students_premise = 114
both_subjects_students_hypothesis = 114

# the hypothesis refers to the same number of students studying certain subjects as mentioned in the premise
if random_processing_students_premise != random_processing_students_hypothesis:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif scramjet_students_hypothesis != scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif both_subjects_students_hypothesis != both_subjects_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

