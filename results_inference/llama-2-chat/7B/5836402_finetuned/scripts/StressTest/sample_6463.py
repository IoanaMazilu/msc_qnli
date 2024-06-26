random_processing_students_premise = 102
scramjet_students_premise = 232
shared_students_premise = 112

random_processing_students_hypothesis = 302
scramjet_students_hypothesis = 232
shared_students_hypothesis = 112

# the hypothesis refers to the number of students studying Random-processing methods, Scramjet rocket engines, and both in the premise
if random_processing_students_premise!= random_processing_students_hypothesis:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif scramjet_students_premise!= scramjet_students_hypothesis:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif shared_students_premise!= shared_students_hypothesis:
    # check if the number of students studying both in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
