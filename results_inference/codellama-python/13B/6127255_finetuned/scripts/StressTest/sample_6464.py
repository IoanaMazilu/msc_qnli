random_processing_students_premise = 302
random_processing_students_hypothesis = 102
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the same faculty, mentioned in the premise
if random_processing_students_hypothesis > random_processing_students_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif both_students_hypothesis!= both_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
