people_premise = 14
people_hypothesis = 14

# the hypothesis talks about the number of people in a BCCI meeting, referenced also in the premise
if people_hypothesis > people_premise:
    # check if the hypothesis value contradicts the exact number of 'people_premise' in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
