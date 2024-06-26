killed_premise = 4
killed_hypothesis = 4
wounded_premise = 80
wounded_hypothesis = 80

# the hypothesis talks about the number of killed and wounded Iraqi guardsmen in a mortar attack, which is also mentioned in the premise
if killed_hypothesis!= killed_premise:
    # check if the number of killed guardsmen in the hypothesis contradicts the number of killed guardsmen from the premise
    label = "contradiction"
elif wounded_hypothesis!= wounded_premise:
    # check if the number of wounded guardsmen in the hypothesis contradicts the number of wounded guardsmen in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
