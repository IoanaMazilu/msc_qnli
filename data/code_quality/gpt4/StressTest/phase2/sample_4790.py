people_premise = 11
people_hypothesis = 61

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_hypothesis == people_premise:
    # check if the number of people in the hypothesis match with the number of people in the premise
    label = "entailment"
else:
    # if the number of people in the hypothesis does not match with the number of people in the premise, it is a contradiction
    label = "contradiction"

print(label)
