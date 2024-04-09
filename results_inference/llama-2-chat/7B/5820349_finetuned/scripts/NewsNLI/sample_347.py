people_viewed_premise = 1200000
people_viewed_hypothesis = 1200000

# the hypothesis mentions the number of people who viewed it, which is also referenced in the premise
if people_viewed_hypothesis!= people_viewed_premise:
    # check if the number of people who viewed it in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of people who viewed it in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
