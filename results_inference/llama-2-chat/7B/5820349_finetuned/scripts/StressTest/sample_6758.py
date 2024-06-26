tom_goes_premise = 8
tom_goes_hypothesis = 6

# the hypothesis talks about the time Tom goes, referenced also in the premise
if tom_goes_hypothesis!= tom_goes_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the time in the hypothesis does not contradict the time in the premise, we can infer entailment
    label = "entailment"

print(label)
