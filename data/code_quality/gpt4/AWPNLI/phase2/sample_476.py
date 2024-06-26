initial_puppies_premise = 6.0
gave_puppies_premise = 2.0
remaining_puppies_hypothesis = 4.0

# the hypothesis refers to the number of puppies Sam has, which is also mentioned in the premise
# compute the number of puppies Sam has after giving some to a friend
remaining_puppies_premise = initial_puppies_premise - gave_puppies_premise

if remaining_puppies_hypothesis != remaining_puppies_premise:
    # check if the number of puppies in the hypothesis contradicts the number of puppies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
