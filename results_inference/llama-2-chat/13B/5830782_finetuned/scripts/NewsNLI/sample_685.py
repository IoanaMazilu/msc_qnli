people_premise = 155
people_hypothesis = 155

# the hypothesis mentions the total number of people aboard the flight, which is also mentioned in the premise
if people_hypothesis!= people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people reported in the premise
    label = "contradiction"
else:
    # if the total number of people in the hypothesis does not contradict the total number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
