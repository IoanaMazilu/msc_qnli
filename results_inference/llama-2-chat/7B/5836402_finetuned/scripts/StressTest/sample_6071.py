builder_days_premise = 15
builder_days_hypothesis = 15

# the hypothesis refers to the number of days the builder takes to build, mentioned in the premise
if builder_days_hypothesis!= builder_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
