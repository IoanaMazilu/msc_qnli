quarters_premise = 33.0
nickels_premise = 87.0
nickels_from_dad_premise = 75.0
nickels_hypothesis = 161.0

# the hypothesis refers to the total number of nickels, which is also part of the premise
# compute the total number of nickels in the premise
total_nickels_premise = nickels_premise + nickels_from_dad_premise
if nickels_hypothesis != total_nickels_premise:
    # check if the total number of nickels in the hypothesis contradicts the total number of nickels from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
