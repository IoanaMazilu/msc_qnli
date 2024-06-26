jim_cleaning_premise = 6
jim_cleaning_hypothesis = 1

if jim_cleaning_hypothesis <= jim_cleaning_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
