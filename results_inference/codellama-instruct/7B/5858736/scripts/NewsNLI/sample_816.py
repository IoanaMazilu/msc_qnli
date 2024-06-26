premise_oppose = 62
hypothesis_oppose = 63

if hypothesis_oppose!= premise_oppose:
    label = "contradiction"
else:
    label = "entailment"

print(label)
