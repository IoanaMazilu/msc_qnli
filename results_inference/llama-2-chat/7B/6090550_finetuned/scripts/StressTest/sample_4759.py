shirts_premise = 5
shirts_hypothesis = 1
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the number of shirts, jeans and sneakers in an outfit
if shirts_premise < shirts_hypothesis:
    # check if the number of shirts in the hypothesis contradicts the premise
    label = "contradiction"
elif jeans_premise!= jeans_hypothesis or sneakers_premise!= sneakers_hypothesis:
    # check if the number of jeans or sneakers in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
