# the hypothesis refers to the number of apples after giving 22 to Mike
# which is not mentioned in the premise

if yhat > 48:
    label = "contradiction"
elif yhat == 48:
    label = "entailment"
else:
    label = "neutral"

print(label)
