# Premise: The 2 nd builder builds in 15 days, then how many 2's are used by the builder from Chennai in numbering the 100 homes?
# Hypothesis: The more than 1 nd builder builds in 15 days, then how many 2's are used by the builder from Chennai in numbering the 100 homes?
# Golden Label: entailment

builder_premise = 2
builder_hypothesis = 1
build_days_premise = 15
build_days_hypothesis = 15
homes_premise = 100
homes_hypothesis = 100

# the hypothesis refers to the number of builders, build days and homes mentioned in the premise
if builder_hypothesis >= builder_premise:
    # check if the builder count in hypothesis contradicts the builder count in premise
    label = "contradiction"
elif build_days_hypothesis != build_days_premise:
    # check if the build days in hypothesis contradicts the build days mentioned in premise
    label = "contradiction"
elif homes_hypothesis != homes_premise:
    # check if the number of homes in hypothesis contradicts the number of homes mentioned in premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

