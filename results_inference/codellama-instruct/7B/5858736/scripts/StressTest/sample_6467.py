peanuts_box_premise = 4
peanuts_box_hypothesis = 2
peanuts_added_premise = 12
peanuts_added_hypothesis = 12

# the hypothesis talks about the number of peanuts in a box, referenced also in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_box_premise'
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)