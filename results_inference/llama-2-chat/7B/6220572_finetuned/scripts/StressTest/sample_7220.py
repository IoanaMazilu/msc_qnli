grade_percentile_premise = 80
grade_percentile_hypothesis = 80

# the hypothesis refers to the percentile of Lena's grade mentioned in the premise
if grade_percentile_hypothesis <= grade_percentile_premise:
    # check if the estimate of 'grade_percentile_hypothesis' contradicts the percentile of Lena's grade reported in the premise
    label = "contradiction"
elif grade_percentile_hypothesis > 100:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
