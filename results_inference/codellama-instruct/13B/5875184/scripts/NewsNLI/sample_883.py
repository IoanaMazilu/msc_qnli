premise_roses = 2
hypothesis_roses = 1

# the hypothesis mentions only one rose, which is less than the number of roses mentioned in the premise
if hypothesis_roses < premise_roses:
    label = "contradiction"
else:
    label = "neutral"

print(label)
