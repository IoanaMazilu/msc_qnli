coins_iron = 5
coins_copper = 5

# The hypothesis mentions the maximum sum, which is also mentioned in the premise
if coins_iron + coins_copper > 35:
    label = "contradiction"
elif coins_iron + coins_copper < 1:
    label = "contradiction"
else:
    label = "entailment"

print(label)
