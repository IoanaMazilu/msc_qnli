people_seated_premise = 8
people_seated_hypothesis = 6

# the hypothesis talks about the number of people seated, which is also mentioned in the premise
if people_seated_hypothesis >= people_seated_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
