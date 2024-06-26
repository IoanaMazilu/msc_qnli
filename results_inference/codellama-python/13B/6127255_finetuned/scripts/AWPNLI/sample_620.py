gallons_premise = 20.0
cans_premise = 5.0
cans_hypothesis = 4.0

# the hypothesis refers to the number of gas cans needed, which can be computed from the premise
# compute the number of gas cans needed from the premise
cans_needed_premise = gallons_premise / cans_premise
if cans_hypothesis!= cans_needed_premise:
    # check if the number of gas cans in the hypothesis contradicts the number of gas cans needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
