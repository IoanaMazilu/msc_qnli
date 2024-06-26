tees_needed_premise = 20
tees_needed_hypothesis = 30
packages_limit_premise = 3
packages_limit_hypothesis = 3

# the hypothesis refers to the number of tees needed and the limit of packages bought mentioned in the premise
if tees_needed_premise >= tees_needed_hypothesis:
    # check if the estimate of 'tees_needed_hypothesis' contradicts the number of tees needed in the premise
    label = "contradiction"
elif packages_limit_hypothesis != packages_limit_premise:
    # check if the limit of packages bought in the hypothesis contradicts the limit of packages bought reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
