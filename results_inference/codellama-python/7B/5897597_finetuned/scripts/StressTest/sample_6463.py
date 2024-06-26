random_processing_students_premise = 102
random_processing_students_hypothesis = 302
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering, mentioned in the premise
if random_processing_students_hypothesis <= random_processing_students_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_students_hypothesis!= both_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying Random-processing methods
    # any number of students greater than 'random_processing_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
