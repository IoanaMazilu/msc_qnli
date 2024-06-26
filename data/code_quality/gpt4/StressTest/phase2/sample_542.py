butter_premise = 3
flour_premise = 4
butter_hypothesis = 6
flour_hypothesis = 4

# The hypothesis and premise both talk about quantities of butter and flour in Elena's bread recipe
if butter_premise == butter_hypothesis and flour_premise == flour_hypothesis:
    # If the quantities of both butter and flour in the hypothesis are the same as in the premise, we can infer entailment
    label = "entailment"
elif butter_premise != butter_hypothesis and flour_premise == flour_hypothesis:
    # If the quantity of butter in the hypothesis contradicts the quantity in the premise, but the quantity of flour is the same, we can infer contradiction
    label = "contradiction"
else:
    # If the quantities of butter and/or flour in the hypothesis do not contradict the premise ones, but also do not match exactly, we can infer neutral
    label = "neutral"

print(label)
