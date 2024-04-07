# Premise: Angela’s grade was in the 90 th percentile out of 80 grades in her class.
# Hypothesis: Angela’s grade was in the more than 40 th percentile out of 80 grades in her class.
# Golden Label: entailment

grade_percentile_premise = 90
grade_percentile_hypothesis = 40
total_grades = 80

# the hypothesis refers to Angela's grade percentile, also mentioned in the premise
if grade_percentile_hypothesis > grade_percentile_premise:
    # check if the grade percentile in the hypothesis contradicts the grade percentile in the premise
    label = "contradiction"
elif grade_percentile_hypothesis == grade_percentile_premise:
    # check if the grade percentile in the hypothesis equals the grade percentile in the premise
    label = "neutral"
else:
    # if the grade percentile in the hypothesis is less than the grade percentile in the premise, we can infer entailment
    label = "entailment"

print(label)

