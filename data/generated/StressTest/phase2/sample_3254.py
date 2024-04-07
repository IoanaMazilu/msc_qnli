# Premise: At the faculty of Aerospace Engineering, 312 students study Random-processing methods, 222 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, less than 312 students study Random-processing methods, 222 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: contradiction

random_processing_students_premise = 312
random_processing_students_hypothesis = 312
scramjet_students_premise = 222
scramjet_students_hypothesis = 222
both_subjects_students_premise = 112
both_subjects_students_hypothesis = 112

# the hypothesis talks about the number of students enrolled in different subjects, referenced also in the premise
if random_processing_students_hypothesis >= random_processing_students_premise:
    # check if the hypothesis value contradicts the estimate of less than 'random_processing_students_hypothesis'
    label = "contradiction"
elif scramjet_students_hypothesis != scramjet_students_premise:
    # check if the number of Scramjet students in the hypothesis contradicts the number of Scramjet students reported in the premise
    label = "contradiction"
elif both_subjects_students_hypothesis != both_subjects_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students studying both subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
