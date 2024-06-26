sailors_premise = 3
sailors_hypothesis = 3

# the hypothesis mentions the same number of sailors as in the premise
if sailors_hypothesis!= sailors_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
