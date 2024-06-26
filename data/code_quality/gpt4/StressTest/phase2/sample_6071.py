builder_premise = 2
builder_hypothesis = 2
build_days_premise = 15
build_days_hypothesis = 15
homes_numbered_premise = 100
homes_numbered_hypothesis = 100

# the hypothesis talks about the builder order, number of days and homes numbered mentioned also in the premise
if builder_hypothesis != builder_premise:
    # check if the builder order in the hypothesis contradicts the builder order in the premise
    label = "contradiction"
elif build_days_hypothesis != build_days_premise:
    # check if the number of build days in the hypothesis contradicts the number of build days reported in the premise
    label = "contradiction"
elif homes_numbered_hypothesis != homes_numbered_premise:
    # check if the number of homes numbered in the hypothesis contradicts the number of homes numbered reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
