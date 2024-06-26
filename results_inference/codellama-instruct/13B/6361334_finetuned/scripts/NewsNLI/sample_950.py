# define variables for the entities in the premise and hypothesis
ng911_premise = "Next Generation 911"
fcc_plan_hypothesis = "FCC plan"

# check if the hypothesis mentions the FCC plan for updating the technology that powers 911 emergency response system
if fcc_plan_hypothesis in ng911_premise:
    # if the hypothesis mentions the FCC plan, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis does not mention the FCC plan, we can infer neutrality
    label = "neutral"

print(label)
