college_graduates_premise = 15
college_graduates_hypothesis = 4

if college_graduates_hypothesis >= college_graduates_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
