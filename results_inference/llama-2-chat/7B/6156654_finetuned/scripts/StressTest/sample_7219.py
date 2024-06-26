grade_percentile_premise = 30
grade_percentile_hypothesis = 80

# the hypothesis refers to the same percentage of grades in Lena's class as the premise
if grade_percentile_premise >= grade_percentile_hypothesis:
    # check if the premise percentage is less than or equal to the hypothesis percentage
    label = "entailment"
elif grade_percentile_premise < grade_percentile_hypothesis:
    # check if the premise percentage is less than the hypothesis percentage
    label = "contradiction"
else:
    # if the premise and hypothesis percentiles are the same, the hypothesis can be inferred from the premise
    label = "neutral"

print(label)
