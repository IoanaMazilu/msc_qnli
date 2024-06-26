shirts_bought_premise = 160
shirts_bought_hypothesis = 160

# the hypothesis talks about the number of shirts bought by Vijay, mentioned also in the premise
if shirts_bought_hypothesis >= shirts_bought_premise:
    # check if the hypothesis value contradicts the premise of buying 'shirts_bought_premise'
    label = "contradiction"
else:
    # if the number of shirts in the hypothesis is less than 'shirts_bought_premise', this can be inferred from the premise
    label = "entailment"

print(label)
