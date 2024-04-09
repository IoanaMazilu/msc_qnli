gang_size_premise = 5
gang_size_hypothesis = int(input("Enter the number of gangs Mala has: "))

# the hypothesis talks about the number of gangs Mala has, referenced also in the premise
if gang_size_hypothesis <= gang_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gang_size_premise'
    label = "contradiction"
elif gang_size_premise == 5:
    # if the premise gives a specific value for the number of gangs, and the hypothesis value is greater, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of gangs
    # any number of gangs greater than 'gang_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
