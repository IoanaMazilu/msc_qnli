# Premise: If there are 4 peanuts in a box and Mary puts 8 more peanuts inside, how many peanuts are in the box?
# Hypothesis: If there are 7 peanuts in a box and Mary puts 8 more peanuts inside, how many peanuts are in the box?
# Golden Label: contradiction

initial_peanuts_premise = 4
added_peanuts_premise = 8
initial_peanuts_hypothesis = 7
added_peanuts_hypothesis = 8

# Both premise and hypothesis discuss the number of peanuts in a box before and after Mary adds some peanuts
if initial_peanuts_premise != initial_peanuts_hypothesis or added_peanuts_premise != added_peanuts_hypothesis:
    # Check if the initial number of peanuts or the number of peanuts added by Mary in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # The initial number of peanuts and those added by Mary in both premise and hypothesis are the same, hence entailment
    label = "entailment"

print(label)

