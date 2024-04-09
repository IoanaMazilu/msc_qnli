ram_shyam_work_premise = 20
ram_shyam_work_hypothesis = 10

# the hypothesis refers to the number of days required to complete the work
if ram_shyam_work_hypothesis > ram_shyam_work_premise:
    # the hypothesis states that the work can be completed in more than the premise, so entailment
    label = "entailment"
elif ram_shyam_work_premise > ram_shyam_work_hypothesis:
    # the premise states that the work can be completed in less than the hypothesis, so contradiction
    label = "contradiction"
else:
    # the hypothesis and premise values are the same, so neutral
    label = "neutral"

print(label)
