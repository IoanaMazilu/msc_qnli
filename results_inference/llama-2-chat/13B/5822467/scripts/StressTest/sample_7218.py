percentile_premise = 80
percentile_hypothesis = 30
grades_premise = 120

# the hypothesis refers to the percentile of Lena's grade in her class
if percentile_hypothesis <= percentile_premise:
    # check if the hypothesis value contradicts the estimate of 'percentile_premise'
    label = "contradiction"
elif percentile_premise!= grades_premise:
    # check if the number of grades in the premise contradicts the number of grades reported in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
