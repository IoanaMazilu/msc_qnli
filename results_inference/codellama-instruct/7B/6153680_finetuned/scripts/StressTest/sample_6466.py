peanuts_box_premise = 1
peanuts_box_hypothesis = 4
peanuts_added_premise = 12
peanuts_added_hypothesis = 12

# the hypothesis talks about the number of peanuts in the box, which is also mentioned in the premise
if peanuts_box_hypothesis!= peanuts_box_premise:
    # check if the number of peanuts in the box in the hypothesis contradicts the number of peanuts in the box in the premise
    label = "contradiction"
else:
    # if the number of peanuts in the box in the hypothesis does not contradict the number of peanuts in the box in the premise
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    if peanuts_added_hypothesis!= peanuts_added_premise:
        label = "contradiction"
    else:
        # if the number of peanuts added in the hypothesis does not contradict the number of peanuts added in the premise
        # we can infer entailment
        label = "entailment"

print(label)
