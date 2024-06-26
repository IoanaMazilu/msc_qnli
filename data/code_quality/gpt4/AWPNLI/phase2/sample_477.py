puppies_premise = 6.0
given_puppies_premise = 2.0
puppies_hypothesis = 8.0

# the hypothesis refers to the number of puppies, which are also mentioned in the premise
# compute the remaining number of puppies in the premise
remaining_puppies_premise = puppies_premise - given_puppies_premise
if puppies_hypothesis != remaining_puppies_premise:
    # check if the number of puppies in the hypothesis contradicts the number of remaining puppies from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
