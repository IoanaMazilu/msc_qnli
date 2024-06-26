premise_percentile = 30
hypothesis_percentile = 80
premise_total_grades = 120
hypothesis_total_grades = 120

# the hypothesis refers to the number of grades in the class and the percentile
if hypothesis_percentile <= premise_percentile:
    # check if the hypothesis value contradicts the estimate of more than 'premise_percentile'
    label = "contradiction"
elif hypothesis_total_grades!= premise_total_grades:
    # check if the number of grades in the hypothesis contradicts the number of grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
