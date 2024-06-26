peanuts_premise = 1
peanuts_hypothesis = 4
peanuts_added_premise = 12
peanuts_added_hypothesis = 12

# the hypothesis talks about the number of peanuts in the box, both in the premise and the hypothesis
if peanuts_premise <= peanuts_hypothesis:
    # check if the number of peanuts in the premise contradicts the number of peanuts in the hypothesis
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
