protesters_premise = 55000
protesters_hypothesis = 55000

# the hypothesis mentions the number of youth protesters in Sanaa, which is also referenced in the premise
if protesters_hypothesis > protesters_premise:
    # check if the number of protesters in the hypothesis contradicts the number of protesters reported in the premise
    label = "contradiction"
elif protesters_hypothesis < protesters_premise:
    # check if the number of protesters from the hypothesis contradicts the number of protesters in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
