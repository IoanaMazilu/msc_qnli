american_literature_mark_premise = 86
american_literature_mark_hypothesis = 66
history_mark_premise = 75
history_mark_hypothesis = 75
home_economics_mark_premise = 52
home_economics_mark_hypothesis = 52
physical_education_mark_premise = 68
physical_education_mark_hypothesis = 68
art_mark_premise = 89
art_mark_hypothesis = 89

# the hypothesis refers to the marks Nancy obtained in each subject, as mentioned in the premise
# the hypothesis values are less than the premise values for all subjects
if american_literature_mark_hypothesis >= american_literature_mark_premise:
    label = "contradiction"
elif history_mark_hypothesis >= history_mark_premise:
    label = "contradiction"
elif home_economics_mark_hypothesis >= home_economics_mark_premise:
    label = "contradiction"
elif physical_education_mark_hypothesis >= physical_education_mark_premise:
    label = "contradiction"
elif art_mark_hypothesis >= art_mark_premise:
    label = "contradiction"
else:
    # if the hypothesis values are less than the premise values, but not contradicting, we can infer entailment
    label = "entailment"

print(label)
