# Premise: At the faculty of Aerospace Engineering, more than 110 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, 310 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: neutral

random_processing_students_premise = 110
random_processing_students_hypothesis = 310
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the same faculty mentioned in the premise
if random_processing_students_hypothesis <= random_processing_students_premise:
    # check if the number of students studying random-processing methods in the hypothesis contradicts the premise estimate
    label = "contradiction"
elif scramjet_students_hypothesis != scramjet_students_premise:
    # check if the number of students studying scramjet rocket engines in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
elif both_students_hypothesis != both_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying random-processing methods
    # any number of students greater than 'random_processing_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

