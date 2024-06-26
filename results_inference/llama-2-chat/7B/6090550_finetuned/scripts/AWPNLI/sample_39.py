 drawer_crayons_premise = 7.0
taken_crayons = 3.0
crayons_left_hypothesis = 0.0

# the hypothesis refers to the number of crayons left in the drawer, which is also mentioned in the premise
# compute the number of crayons left in the drawer according to the hypothesis
crayons_left_premise = drawer_crayons_premise - taken_crayons
if crayons_left_hypothesis!= crayons_left_premise:
    # check if the number of crayons left in the drawer according to the hypothesis contradicts the number of crayons left in the drawer according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
