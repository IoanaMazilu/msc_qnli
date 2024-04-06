# Premise: Britain has about 4,100 troops in Iraq, the second-largest contingent after the United States, which has about 142,500.
# Hypothesis: After U.S.'s 142,500 troops, Britain has second-largest contingent:4,100.
# Golden Label: entailment

britain_troops_premise = 4100
britain_troops_hypothesis = 4100
us_troops_premise = 142500
us_troops_hypothesis = 142500

# the hypothesis mentions the number of troops Britain and the U.S. have in Iraq, which is also referenced in the premise
if britain_troops_hypothesis != britain_troops_premise:
    # check if the number of Britain troops in the hypothesis contradicts the number of Britain troops reported in the premise
    label = "contradiction"
elif us_troops_hypothesis != us_troops_premise:
    # check if the number of U.S. troops from the hypothesis contradicts the number of U.S. troops in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

