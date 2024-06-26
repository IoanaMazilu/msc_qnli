victims_premise = 21
injuries_premise = 35
victims_hypothesis = 21
injuries_hypothesis = 35

# the hypothesis mentions the number of victims and injuries, which are also mentioned in the premise
if victims_hypothesis!= victims_premise:
    # check if the number of victims from the hypothesis contradicts the number of victims in the premise
    label = "contradiction"
elif injuries_hypothesis!= injuries_premise:
    # check if the number of injuries from the hypothesis contradicts the number of injuries in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
