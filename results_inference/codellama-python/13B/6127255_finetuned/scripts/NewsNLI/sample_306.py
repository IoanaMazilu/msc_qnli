britain_troops_premise = 4100
us_troops_premise = 142500
britain_troops_hypothesis = 4100
us_troops_hypothesis = 142500

# the hypothesis mentions the number of Britain's and the U.S.'s troops, which are also mentioned in the premise
if us_troops_hypothesis!= us_troops_premise:
    # check if the number of U.S. troops in the hypothesis contradicts the number of U.S. troops reported in the premise
    label = "contradiction"
elif britain_troops_hypothesis!= britain_troops_premise:
    # check if the number of Britain's troops from the hypothesis contradicts the number of Britain's troops in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
