premise_discount = 20
hypothesis_discount = 50

# the hypothesis talks about a different discount than the premise
if hypothesis_discount!= premise_discount:
    # the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis values are consistent
    label = "neutral"

print(label)
