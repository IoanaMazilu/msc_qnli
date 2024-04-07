# Premise: If there are less than 5 peanuts in a box and Mary puts 6 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are 4 peanuts in a box and Mary puts 6 more peanuts inside, how many peanuts are in the box?
# Golden Label: neutral

peanuts_box_premise = 5
peanuts_added_premise = 6
peanuts_box_hypothesis = 4
peanuts_added_hypothesis = 6

# the hypothesis refers to the number of peanuts in a box and the number of peanuts added, both mentioned in the premise
if peanuts_box_hypothesis >= peanuts_box_premise:
    # check if the number of peanuts in the box in the hypothesis contradicts the premise, which states there are less than 'peanuts_box_premise' peanuts
    label = "contradiction"
elif peanuts_added_hypothesis != peanuts_added_premise:
    # check if the number of peanuts added in the hypothesis contradicts the number of peanuts added in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

