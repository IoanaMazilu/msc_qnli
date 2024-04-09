britain_troops_premise = 4100
us_troops_premise = 142500
britain_troops_hypothesis = 4100
us_troops_hypothesis = 142500

# the hypothesis mentions the number of British troops after the U.S. troops, which is also referenced in the premise
if britain_troops_hypothesis!= britain_troops_premise:
    # check if the number of British troops in the hypothesis contradicts the number of British troops in the premise
    label = "contradiction"
elif us_troops_hypothesis!= us_troops_premise:
    # check if the number of U.S. troops from the hypothesis contradicts the number of U.S. troops in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
