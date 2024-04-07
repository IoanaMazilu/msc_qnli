# Premise: If there are less than 8 peanuts in a box and Mary puts 4 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are 4 peanuts in a box and Mary puts 4 more peanuts inside, how many peanuts are in the box?
# Golden Label: neutral

peanuts_box_premise = 8
added_peanuts = 4
peanuts_box_hypothesis = 4

# The hypothesis refers to the number of peanuts in the box and the number of peanuts added, both mentioned in the premise
if peanuts_box_hypothesis >= peanuts_box_premise:
    # check if the hypothesis value contradicts the estimate of less than 'peanuts_box_premise'
    label = "contradiction"
elif peanuts_box_hypothesis + added_peanuts != peanuts_box_premise + added_peanuts:
    # check if the number of total peanuts in the box after adding in hypothesis contradicts the number of total peanuts in the box after adding in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

