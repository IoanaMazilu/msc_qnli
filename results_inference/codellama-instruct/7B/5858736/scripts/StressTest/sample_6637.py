# Define variables for the numerical entities in the premise and hypothesis
ram_days_premise = 50
krish_days_premise = 50
bhim_days_premise = 50

ram_days_hypothesis = 30
krish_days_hypothesis = 30
bhim_days_hypothesis = 30

# Check if the hypothesis values contradict the premise
if ram_days_hypothesis > ram_days_premise:
    label = "contradiction"
elif krish_days_hypothesis > krish_days_premise:
    label = "contradiction"
elif bhim_days_hypothesis > bhim_days_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
