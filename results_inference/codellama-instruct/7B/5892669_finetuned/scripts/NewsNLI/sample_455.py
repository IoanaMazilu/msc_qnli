arrested_people_premise = 52
arrested_people_hypothesis = 52

# the hypothesis mentions the number of people arrested in Philadelphia, which is also referenced in the premise
if arrested_people_hypothesis!= arrested_people_premise:
    # check if the number of arrested people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of arrested people in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)