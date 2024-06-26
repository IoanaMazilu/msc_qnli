peanuts_in_box_premise = 4
peanuts_added_premise = 12
peanuts_in_box_hypothesis = 2
peanuts_added_hypothesis = 12

# the hypothesis talks about the number of peanuts in a box and the number of peanuts added, referenced also in the premise
if peanuts_in_box_hypothesis!= peanuts_in_box_premise:
    # check if the number of peanuts in the hypothesis contradicts the number of peanuts in the premise
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
