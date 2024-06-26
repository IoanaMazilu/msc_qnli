premise_plan = "NG911"
hypothesis_plan = "FCC plan"

# the hypothesis mentions the name of the plan, which is also mentioned in the premise
if hypothesis_plan!= premise_plan:
    # check if the name of the plan in the hypothesis contradicts the name of the plan in the premise
    label = "contradiction"
else:
    # if the name of the plan in the hypothesis does not contradict the name of the plan in the premise, we can infer entailment
    label = "entailment"

print(label)
