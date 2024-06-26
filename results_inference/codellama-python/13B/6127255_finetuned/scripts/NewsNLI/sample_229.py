wounded_premise = 1000
wounded_hypothesis = 1000
killed_premise = 1
killed_hypothesis = 6

# the hypothesis mentions the number of killed and wounded people, which are also mentioned in the premise
if killed_hypothesis!= killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people reported in the premise
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # check if the number of wounded people from the hypothesis contradicts the number of wounded people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
