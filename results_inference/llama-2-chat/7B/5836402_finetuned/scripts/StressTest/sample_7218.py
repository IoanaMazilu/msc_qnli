grade_premise = 80
grade_hypothesis = 30
grades_premise = 120
grades_hypothesis = 120

# the hypothesis refers to the grade percentile of Lena mentioned in the premise
if grade_hypothesis <= grade_premise:
    # check if the estimate of 'grade_hypothesis' contradicts the grade percentile in the premise
    label = "contradiction"
elif grade_hypothesis > grade_premise:
    # check if the grade percentile in the hypothesis is greater than the percentile in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
