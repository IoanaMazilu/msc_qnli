grade_percentile_premise = 80
grade_percentile_hypothesis = 80

# the hypothesis refers to the same grade percentile as the premise
if grade_percentile_hypothesis!= grade_percentile_premise:
    # check if the hypothesis grade percentile is less than the premise grade percentile
    label = "contradiction"
else:
    # if the hypothesis grade percentile is the same as the premise grade percentile, it's an entailment
    label = "entailment"

print(label)
