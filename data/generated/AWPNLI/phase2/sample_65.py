# Premise: Mike had 33.0 quarters and 87.0 nickels in his bank and his dad borrowed 75.0 nickels from Mike.
# Hypothesis: He has 14.0 nickels now.
# Golden Label: contradiction

quarters_premise = 33.0
nickels_premise = 87.0
nickels_borrowed_premise = 75.0
nickels_hypothesis = 14.0

# the hypothesis refers to the number of nickels, which are also mentioned in the premise
# compute the current number of nickels in the premise
current_nickels_premise = nickels_premise - nickels_borrowed_premise

if nickels_hypothesis != current_nickels_premise:
    # check if the number of nickels in the hypothesis contradicts the number of nickels from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

