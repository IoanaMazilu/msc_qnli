percentile_premise = 80
percentile_hypothesis = 80
grades_premise = 120
grades_hypothesis = 120

# the hypothesis talks about Lena's grade in the same class, so we can infer the same percentile and number of grades
if percentile_hypothesis!= percentile_premise:
    # check if the percentile in the hypothesis contradicts the percentile in the premise
    label = "contradiction"
elif grades_hypothesis!= grades_premise:
    # check if the number of grades in the hypothesis contradicts the number of grades in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
