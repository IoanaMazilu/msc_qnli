ram_work_premise = 40
ram_work_hypothesis = 60
bhim_work_premise = None

# the premise talks about the work that can be completed by Ram and Krish together
if ram_work_hypothesis > ram_work_premise:
    # the hypothesis states that Ram and Krish can complete the work in more than 40 days, which contradicts the premise
    label = "contradiction"
elif bhim_work_premise is None or bhim_work_premise > ram_work_hypothesis:
    # the premise does not provide information about Bhim's work, so we cannot infer entailment or contradiction
    label = "neutral"
else:
    # the hypothesis states that Bhim will take longer than Ram and Krish to complete the work
    # we can infer entailment as the hypothesis is consistent with the premise
    label = "entailment"

print(label)
