# Premise: If there are 4 peanuts in a box and Mary puts 6 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are less than 4 peanuts in a box and Mary puts 6 more peanuts inside, how many peanuts are in the box?
# Golden Label: contradiction

initial_peanuts_premise = 4
added_peanuts_premise = 6
initial_peanuts_hypothesis = 4

# the hypothesis refers to the initial number of peanuts in the box mentioned in the premise
if initial_peanuts_hypothesis >= initial_peanuts_premise:
    # check if the hypothesis value contradicts the premise's explicit statement
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

