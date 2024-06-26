people_premise = 10
people_hypothesis = 10

# the hypothesis talks about the number of people in the room, which is also referenced in the premise
# check if the number of people in the premise contradicts the number of people in the hypothesis
if people_premise!= people_hypothesis:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
