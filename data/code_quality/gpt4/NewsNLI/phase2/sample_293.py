malaga_status_premise = "debutants"
dortmund_status_premise = "1997 winners"
malaga_status_hypothesis = "debutants"
dortmund_status_hypothesis = "1997 champions"

# the hypothesis mentions the status of Malaga and Borussia Dortmund, which are also mentioned in the premise
if malaga_status_hypothesis != malaga_status_premise:
    # check if the status of Malaga in the hypothesis contradicts the status reported in the premise
    label = "contradiction"
elif dortmund_status_hypothesis != dortmund_status_premise:
    # check if the status of Dortmund from the hypothesis contradicts the status of Dortmund in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
