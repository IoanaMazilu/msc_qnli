shirts_premise = 4
shirts_hypothesis = 1
jeans_premise = 1
jeans_hypothesis = 1
sneakers_premise = 1
sneakers_hypothesis = 1

# the hypothesis talks about the number of shirts, jeans and sneakers in an outfit, referenced also in the premise
if shirts_hypothesis >= shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirts_premise'
    label = "contradiction"
elif jeans_hypothesis!= jeans_premise or sneakers_hypothesis!= sneakers_premise:
    # check if the number of jeans or sneakers in the hypothesis contradicts the number of jeans or sneakers in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts less than'shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
