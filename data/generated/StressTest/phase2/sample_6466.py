# Premise: If there are more than 1 peanuts in a box and Mary puts 12 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are 4 peanuts in a box and Mary puts 12 more peanuts inside, how many peanuts are in the box?
# Golden Label: neutral

peanuts_premise = 1
peanuts_hypothesis = 4
add_peanuts = 12

# the hypothesis talks about the number of peanuts in a box, referenced also in the premise
if peanuts_hypothesis <= peanuts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'peanuts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of peanuts
    # any number of peanuts greater than 'peanuts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

