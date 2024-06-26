days_to_save_premise = 80
days_to_save_hypothesis = 30

# The hypothesis mentions the number of days Lexi needed to save to afford a vacation, which is also mentioned in the premise
if days_to_save_hypothesis >= days_to_save_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # If the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
