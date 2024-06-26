percentile_premise = 80
percentile_hypothesis = 80
grades_premise = 120
grades_hypothesis = 120

# the hypothesis refers to Lena's grade percentile and the number of grades in the class, both mentioned in the premise
if percentile_hypothesis <= percentile_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif grades_hypothesis!= grades_premise:
    # check if the number of grades in the class in the hypothesis contradicts the number of grades reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
