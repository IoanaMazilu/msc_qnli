peanuts_box_premise = 1
peanuts_added_premise = 8
peanuts_box_hypothesis = 4
peanuts_added_hypothesis = 8

# the hypothesis talks about the number of peanuts in a box and the number of peanuts added, referenced also in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_box_premise'
    label = "contradiction"
elif peanuts_added_hypothesis!= peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
