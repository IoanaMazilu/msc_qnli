# Premise: If there are 4 peanuts in a box and Mary puts 12 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are more than 1 peanuts in a box and Mary puts 12 more peanuts inside, how many peanuts are in the box?
# Golden Label: entailment

initial_peanuts_premise = 4
added_peanuts_premise = 12
initial_peanuts_hypothesis = 1
added_peanuts_hypothesis = 12

# the hypothesis talks about the number of peanuts in a box, referenced also in the premise
if initial_peanuts_hypothesis > initial_peanuts_premise:
    # check if the initial number of peanuts in the hypothesis contradicts the initial number of peanuts in the premise
    label = "contradiction"
elif added_peanuts_hypothesis != added_peanuts_premise:
    # check if the added number of peanuts in the hypothesis contradicts the added number of peanuts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

