random_processing_students_premise = 110
random_processing_students_hypothesis = 310
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_subjects_students_premise = 112
both_subjects_students_hypothesis = 112

# the hypothesis talks about the number of students enrolled in certain subjects, referenced also in the premise
if random_processing_students_hypothesis <= random_processing_students_premise:
    # check if the hypothesis value contradicts the estimate of more than 'random_processing_students_premise'
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise or both_subjects_students_hypothesis!= both_subjects_students_premise:
    # check if the number of students enrolled in Scramjet rocket engines or both subjects in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students enrolled in Random-processing methods
    # any number of students greater than 'random_processing_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
