# Premise: Mike had 33.0 quarters and 87.0 nickels in his bank and his dad borrowed 75.0 nickels from Mike.
# Hypothesis: He has 12.0 nickels now.
# Golden Label: entailment

quarters_premise = 33.0
nickels_premise = 87.0
borrowed_nickels_premise = 75.0
nickels_hypothesis = 12.0

# the hypothesis refers to the current number of nickels, which is also mentioned in the premise
# compute the current number of nickels in the premise
current_nickels_premise = nickels_premise - borrowed_nickels_premise
if nickels_hypothesis != current_nickels_premise:
    # check if the number of nickels in the hypothesis contradicts the current number of nickels from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

