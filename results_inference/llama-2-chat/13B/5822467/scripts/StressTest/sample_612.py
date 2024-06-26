gang_size_premise = 8
gang_size_hypothesis = 7

# the hypothesis talks about the number of people in Andrew's friendship gang
if gang_size_hypothesis <= gang_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'gang_size_premise'
    label = "contradiction"
elif gang_size_hypothesis > gang_size_premise:
    # the premise gives only an estimate for the number of people in the gang
    # any number of people greater than 'gang_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
