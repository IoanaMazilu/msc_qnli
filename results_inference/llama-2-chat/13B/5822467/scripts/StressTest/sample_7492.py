peanuts_box_premise = 1 # more than 1 peanut
peanuts_box_hypothesis = 4 # 4 peanuts
mary_adds_premise = 8 # Mary adds 8 more peanuts

# the hypothesis refers to the number of peanuts in the box, as in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of 'peanuts_box_premise'
    label = "contradiction"
elif peanuts_box_hypothesis > peanuts_box_premise:
    # the hypothesis value is greater than the premise estimate, so we can entail the hypothesis from the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of peanuts in the box
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
