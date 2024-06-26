peanuts_box_premise = 1
peanuts_box_hypothesis = 4
additional_peanuts_premise = 12
additional_peanuts_hypothesis = 12

# the hypothesis refers to the number of peanuts in a box and the additional peanuts put inside, both mentioned in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_box_premise'
    label = "contradiction"
elif additional_peanuts_hypothesis!= additional_peanuts_premise:
    # check if the additional peanuts in the hypothesis contradicts the additional peanuts reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
