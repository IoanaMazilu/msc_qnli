# Premise: Lena’s grade was in the 80 th percentile out of 120 grades in her class.
# Hypothesis: Lena’s grade was in the more than 80 th percentile out of 120 grades in her class.
# Golden Label: contradiction

grade_percentile_premise = 80
grade_percentile_hypothesis = 80
total_grades = 120

# the hypothesis talks about Lena's grade percentile, also mentioned in the premise
if grade_percentile_hypothesis != grade_percentile_premise:
    # check if the hypothesis value contradicts the percentile of grades in the premise
    label = "contradiction"
elif grade_percentile_hypothesis == grade_percentile_premise:
    # if the percentile values in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

