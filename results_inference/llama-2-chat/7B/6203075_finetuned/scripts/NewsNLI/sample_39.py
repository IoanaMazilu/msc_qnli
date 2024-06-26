people_joining_premise = 200
people_gathered_hypothesis = 200

# the hypothesis mentions the number of people gathered to ride with Armstrong, which is also mentioned in the premise
if people_joining_premise!= people_gathered_hypothesis:
    # check if the number of people gathered in the hypothesis contradicts the number of people joining Armstrong in the premise
    label = "contradiction"
else:
    # if the number of people gathered in the hypothesis does not contradict the number of people joining Armstrong in the premise, we can infer entailment
    label = "entailment"

print(label)
