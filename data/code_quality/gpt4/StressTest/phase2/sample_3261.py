peanuts_in_box_premise = 4
peanuts_added_premise = 2
peanuts_in_box_hypothesis = 3
peanuts_added_hypothesis = 2

# hypothesis makes a general statement about a case where there are more than 3 peanuts in a box
if peanuts_in_box_premise <= peanuts_in_box_hypothesis:
    # check if the number of peanuts in the box in the premise contradicts the hypothesis
    label = "contradiction"
elif peanuts_added_premise != peanuts_added_hypothesis:
    # check if the number of peanuts added in the hypothesis contradicts the number added in the premise
    label = "contradiction"
else:
    # if the variables in the hypothesis do not contradict those in the premise, we can infer entailment
    label = "entailment"

print(label)
