ng911_plan_premise = "five-step plan"
ng911_plan_hypothesis = "update technology"

# check if the hypothesis mentions a different aspect of the NG911 plan than the premise
if ng911_plan_hypothesis!= ng911_plan_premise:
    # if the hypothesis mentions a different aspect, it contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis and premise mention the same aspect, we can infer entailment
    label = "entailment"

print(label)
