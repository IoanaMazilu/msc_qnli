cats_start_premise = 17.0
cats_given_premise = 14.0
cats_hypothesis = 5.0

# the hypothesis refers to the number of cats, which are also mentioned in the premise
# compute the remaining number of cats in the premise
cats_remaining_premise = cats_start_premise - cats_given_premise
if cats_hypothesis!= cats_remaining_premise:
    # check if the number of cats in the hypothesis contradicts the number of cats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
