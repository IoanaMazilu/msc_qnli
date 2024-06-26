random_processing_students_premise = 112
scramjet_students_premise = 234
both_students_premise = 112

random_processing_students_hypothesis = 312
scramjet_students_hypothesis = 234
both_students_hypothesis = 112

# the hypothesis talks about the number of students studying Random-processing methods, Scramjet rocket engines, and both, referenced also in the premise
if random_processing_students_hypothesis!= random_processing_students_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
elif scramjet_students_hypothesis!= scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
elif both_students_hypothesis!= both_students_premise:
    # check if the number of students studying both in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
