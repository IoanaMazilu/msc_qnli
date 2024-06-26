victims_premise = 3
injuries_premise = 52

victims_hypothesis = 3
injuries_hypothesis = 52

# the hypothesis mentions the number of victims and injured people, which are also mentioned in the premise
if victims_hypothesis!= victims_premise:
    # check if the number of victims from the hypothesis contradicts the number of victims in the premise
    label = "contradiction"
elif injuries_hypothesis!= injuries_premise:
    # check if the number of injured people from the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
