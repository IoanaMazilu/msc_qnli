peanuts_premise = 4
peanuts_added_premise = 2
peanuts_hypothesis = 7
peanuts_added_hypothesis = 2

# the hypothesis talks about the number of peanuts in a box and the number added, referenced also in the premise
if peanuts_premise != peanuts_hypothesis:
    # check if the initial number of peanuts in the hypothesis contradicts the initial number of peanuts in the premise
    label = "contradiction"
elif peanuts_added_premise != peanuts_added_hypothesis:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, it is still impossible to infer an entailment as the final count of peanuts is not specified in either the premise or the hypothesis
    label = "neutral"

print(label)
