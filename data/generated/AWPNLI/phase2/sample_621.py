# Premise: I want to put 20.0 gallons of gas into 5.0 gallon gas cans.
# Hypothesis: I need 3.0 gas cans.
# Golden Label: contradiction

gas_gallons_premise = 20.0
gas_cans_capacity_premise = 5.0
gas_cans_needed_hypothesis = 3.0

# the hypothesis refers to the number of gas cans needed, which are also mentioned in the premise
# compute the number of gas cans needed in the premise
gas_cans_needed_premise = gas_gallons_premise / gas_cans_capacity_premise
if gas_cans_needed_hypothesis != gas_cans_needed_premise:
    # check if the number of gas cans in the hypothesis contradicts the number of gas cans needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

