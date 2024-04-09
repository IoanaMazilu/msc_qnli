deceased_premise = 12
victims_premise = 5

# define variables for the hypothesis values
deceased_hypothesis = 12
victims_hypothesis = 5

# compare the number of deceased and victims in the hypothesis with the premise
if deceased_hypothesis!= deceased_premise or victims_hypothesis!= victims_premise:
    # if the hypothesis values contradict the premise values, label the comparison as "contradiction"
    label = "contradiction"
else:
    # if the hypothesis values match the premise values, label the comparison as "entailment"
    label = "entailment"

print(label)
