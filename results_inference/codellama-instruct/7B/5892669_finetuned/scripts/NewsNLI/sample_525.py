experts_premise = 1
experts_hypothesis = 1

# the hypothesis mentions the number of experts who say open-source anti-bribe sites pose serious ethical questions, which is also referenced in the premise
if experts_hypothesis!= experts_premise:
    # check if the number of experts in the hypothesis contradicts the number of experts mentioned in the premise
    label = "contradiction"
else:
    # if the number of experts in the hypothesis does not contradict the number of experts in the premise, we can infer entailment
    label = "entailment"

print(label)
