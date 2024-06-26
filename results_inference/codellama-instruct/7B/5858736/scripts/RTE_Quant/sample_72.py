denmark_premise = 3
sweden_premise = 3
britain_premise = 3
euro_premise = 1999

denmark_hypothesis = 1
sweden_hypothesis = 1
britain_hypothesis = 1
euro_hypothesis = 1999

if denmark_hypothesis!= denmark_premise or sweden_hypothesis!= sweden_premise or britain_hypothesis!= britain_premise:
    label = "contradiction"
elif euro_hypothesis!= euro_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
