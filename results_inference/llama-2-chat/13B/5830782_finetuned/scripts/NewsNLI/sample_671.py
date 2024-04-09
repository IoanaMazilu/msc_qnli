inmates_premise = 200  # maximum number of escaped inmates according to the premise
inmates_hypothesis = 200  # maximum number of escaped inmates according to the hypothesis

# the hypothesis mentions a possible number of escaped inmates, which is also mentioned in the premise
if inmates_hypothesis > inmates_premise:
    # check if the number of escaped inmates in the hypothesis contradicts the maximum number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
