employees_premise = 250
employees_hypothesis = 850

# the hypothesis refers to the number of employees at Veridux Corporation, mentioned in the premise
if employees_premise <= employees_hypothesis:
    # check if the estimate of 'employees_hypothesis' contradicts the number of employees reported in the premise
    label = "contradiction"
elif employees_hypothesis - employees_premise > 500:
    # check if the difference between the hypothesis and premise values is greater than 500
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
