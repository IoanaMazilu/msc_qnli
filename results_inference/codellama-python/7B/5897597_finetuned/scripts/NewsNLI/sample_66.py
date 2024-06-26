requests_premise = 2
requests_hypothesis = 2

# the hypothesis mentions the number of requests from CNN, which is also referenced in the premise
if requests_hypothesis!= requests_premise:
    # check if the number of requests in the hypothesis contradicts the number of requests reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
