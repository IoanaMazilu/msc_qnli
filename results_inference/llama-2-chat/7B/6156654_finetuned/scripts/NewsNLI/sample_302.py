# The premise and hypothesis are similar, but the hypothesis is more specific
label = "entailment"

# The premise mentions that Google will provide nutrition info for more than 1,000 foods, which is also mentioned in the hypothesis
if premise_foods_count > 1000:
    # The hypothesis specifies the exact number of foods, which is also mentioned in the premise
    label = "contradiction"
else:
    # If the number of foods in the hypothesis is less than the number in the premise, we can infer entailment
    label = "entailment"

print(label)
