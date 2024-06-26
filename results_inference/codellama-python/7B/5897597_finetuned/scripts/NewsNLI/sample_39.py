people_premise = 200
people_hypothesis = 200

# the hypothesis mentions the number of people who gathered in Paisley High Street to ride with Armstrong, which is also mentioned in the premise
if people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # if the number of people in the hypothesis does not contradict the number of people in the premise, we can infer entailment
    label = "entailment"

print(label)
