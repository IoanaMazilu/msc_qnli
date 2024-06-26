children_test_premise = 698.0
passed_premise = 105.0
sit_again_hypothesis = 591.0

# the hypothesis refers to the number of children who had to sit the test again, which can be inferred from the premise
# compute the number of children who had to sit the test again in the premise
sit_again_premise = children_test_premise - passed_premise
if sit_again_hypothesis != sit_again_premise:
    # check if the number of children who had to sit the test again in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
