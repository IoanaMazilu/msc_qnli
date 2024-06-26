people_viewed_premise = 1.2e6
people_viewed_hypothesis = 1.2e6

# the hypothesis mentions the number of people who have viewed it on YouTube, which is also referenced in the premise
if people_viewed_hypothesis!= people_viewed_premise:
    # check if the number of people viewed in the hypothesis contradicts the number of people viewed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
