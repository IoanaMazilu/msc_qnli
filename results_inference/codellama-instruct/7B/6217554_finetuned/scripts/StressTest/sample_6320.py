apples_maddie_premise = 4
apples_maddie_hypothesis = 6

# the hypothesis gives the exact number of apples Maddie has
if apples_maddie_hypothesis!= apples_maddie_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
