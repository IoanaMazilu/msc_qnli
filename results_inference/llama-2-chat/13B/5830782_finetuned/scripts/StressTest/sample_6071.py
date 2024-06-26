builder_premise = 2
builder_hypothesis = 2
build_days_premise = 15
build_days_hypothesis = 15
homes_premise = 100
homes_hypothesis = 100

# the hypothesis refers to the builder, build days and number of homes mentioned in the premise
if builder_premise >= builder_hypothesis:
    # check if the builder's number in the hypothesis contradicts the builder's number in the premise
    label = "contradiction"
elif build_days_premise!= build_days_hypothesis:
    # check if the build days in the hypothesis contradicts the build days reported in the premise
    label = "contradiction"
elif homes_premise!= homes_hypothesis:
    # check if the number of homes in the hypothesis contradicts the number of homes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
