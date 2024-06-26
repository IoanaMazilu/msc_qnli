# There are no numerical entities in the premise or hypothesis to compare
# Therefore, we cannot perform an exact entailment check

# However, we can check if the hypothesis contradicts the premise
if "two attack helicopters" in hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
