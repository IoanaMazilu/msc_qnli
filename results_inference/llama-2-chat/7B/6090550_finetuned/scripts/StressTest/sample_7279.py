y = 210

### Premise
employees_premise = 510

### Hypothesis
employees_hypothesis = 210

### Checking if the hypothesis contradicts the premise
if employees_hypothesis >= employees_premise:
    # The hypothesis value contradicts the premise, so we can infer entailment
    label = "entailment"
else:
    # The hypothesis value is less than the premise, so we can infer neutrality
    label = "neutral"

print(label)


