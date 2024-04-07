# Premise: If there are more than 3 peanuts in a box and Mary puts 2 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are 4 peanuts in a box and Mary puts 2 more peanuts inside, how many peanuts are in the box?
# Golden Label: neutral

peanuts_box_premise = 3
peanuts_added_premise = 2
peanuts_box_hypothesis = 4
peanuts_added_hypothesis = 2

# the hypothesis talks about the number of peanuts in a box before and after Mary adds some, referenced also in the premise
if peanuts_box_hypothesis <= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_box_premise'
    label = "contradiction"
elif peanuts_added_hypothesis != peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts before adding
    # any number of peanuts greater than 'peanuts_box_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

