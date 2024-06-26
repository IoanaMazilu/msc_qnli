premise_grade = 80
premise_total_grades = 120
hypothesis_grade = 80
hypothesis_total_grades = 120

# the hypothesis refers to the grade and total number of grades mentioned in the premise
if hypothesis_grade > premise_grade:
    # check if the estimate of 'hypothesis_grade' contradicts the grade in the premise
    label = "contradiction"
elif hypothesis_total_grades!= premise_total_grades:
    # check if the number of total grades in the hypothesis contradicts the number of total grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
