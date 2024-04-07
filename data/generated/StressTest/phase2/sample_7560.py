# Premise: At the faculty of Aerospace Engineering, 310 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, more than 110 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: entailment

random_processing_students_premise = 310
random_processing_students_hypothesis = 110
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_courses_students_premise = 112
both_courses_students_hypothesis = 112

# the hypothesis refers to the number of students studying different courses at the faculty of Aerospace Engineering, as mentioned in the premise
if random_processing_students_premise <= random_processing_students_hypothesis:
    # check if the estimate of 'random_processing_students_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif scramjet_students_hypothesis != scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_courses_students_hypothesis != both_courses_students_premise:
    # check if the number of students studying both courses in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

