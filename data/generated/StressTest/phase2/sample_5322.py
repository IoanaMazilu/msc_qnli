# Premise: If there are 4 peanuts in a box and Mary puts 6 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are less than 5 peanuts in a box and Mary puts 6 more peanuts inside, how many peanuts are in the box?
# Golden Label: entailment

peanuts_box_premise = 4
peanuts_added = 6
peanuts_box_hypothesis = 5

# the hypothesis refers to the initial number of peanuts in a box, which is also mentioned in the premise
if peanuts_box_premise >= peanuts_box_hypothesis:
    # check if the initial number of peanuts in the premise contradicts the estimate of less than 'peanuts_box_hypothesis'
    label = "contradiction"
else:
    # if the initial number of peanuts does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

