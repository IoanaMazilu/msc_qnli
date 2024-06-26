killed_premise = 4
wounded_premise = 80
killed_hypothesis = 4
wounded_hypothesis = 80

# the hypothesis talks about the number of killed and wounded people in a mortar attack, which is also mentioned in the premise
if killed_hypothesis!= killed_premise:
    # check if the number of killed people in the hypothesis contradicts the number of killed people from the premise
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # check if the number of wounded people in the hypothesis contradicts the number of wounded people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
