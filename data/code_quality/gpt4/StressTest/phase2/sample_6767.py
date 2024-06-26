people_premise = 13
people_hypothesis = 13

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_hypothesis < people_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
elif people_hypothesis == people_premise:
    # check if the hypothesis value is the same as the number of people in the premise
    label = "entailment"
else:
    # if the hypothesis value is greater than the number of people in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
