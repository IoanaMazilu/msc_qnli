youth_protesters_premise = 55000
youth_protesters_hypothesis = 55000

# the hypothesis mentions the number of youth protesters in Sanaa, which is also referenced in the premise
if youth_protesters_hypothesis > youth_protesters_premise:
    # check if the number of youth protesters in the hypothesis contradicts the number of youth protesters in the premise
    label = "contradiction"
else:
    # if the number of youth protesters in the hypothesis does not contradict the number of youth protesters in the premise, we can infer entailment
    label = "entailment"

print(label)
