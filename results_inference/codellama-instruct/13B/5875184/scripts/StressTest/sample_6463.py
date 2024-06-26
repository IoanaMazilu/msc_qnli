premise_students_random = 102
premise_students_scramjet = 232
premise_students_both = 112

hypothesis_students_random = 302
hypothesis_students_scramjet = 232
hypothesis_students_both = 112

# the hypothesis refers to the number of students studying Random-processing methods, Scramjet rocket engines and both
if hypothesis_students_random <= premise_students_random:
    # check if the estimate of 'hypothesis_students_random' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif hypothesis_students_scramjet!= premise_students_scramjet:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
elif hypothesis_students_both!= premise_students_both:
    # check if the number of students studying both Random-processing methods and Scramjet rocket engines in the hypothesis contradicts the number of students studying both reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
