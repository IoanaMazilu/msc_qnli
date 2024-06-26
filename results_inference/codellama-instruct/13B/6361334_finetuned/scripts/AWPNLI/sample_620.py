gallons_premise = 20.0
gas_cans_premise = 5.0
gallons_hypothesis = 4.0

# the hypothesis refers to the number of gas cans, which are also mentioned in the premise
# compute the total number of gallons in the premise
total_gallons_premise = gallons_premise / gas_cans_premise
if total_gallons_hypothesis > total_gallons_premise:
    # check if the number of gallons in the hypothesis contradicts the number of gallons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
