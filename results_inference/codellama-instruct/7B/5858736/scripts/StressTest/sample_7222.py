# the hypothesis talks about the number of students and grades in a class, referenced also in the premise
if hypothesis_students <= premise_students:
    # check if the hypothesis value contradicts the estimate of less than 'premise_students'
    label = "contradiction"
elif hypothesis_grades_higher_than_lena <= premise_grades_higher_than_lena:
    # check if the hypothesis value contradicts the estimate of 'premise_grades_higher_than_lena'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
