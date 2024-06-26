apples_premise = 7
apples_hypothesis = 4
given_to_mike_premise = 2
given_to_mike_hypothesis = 2

# the hypothesis talks about the number of apples Maddie has and the number of apples given to Mike, both referenced in the premise
if apples_hypothesis >= apples_premise:
    # check if the hypothesis value contradicts the estimate of less than 'apples_premise'
    label = "contradiction"
elif given_to_mike_hypothesis!= given_to_mike_premise:
    # check if the number of apples given to Mike in the hypothesis contradicts the number of apples given to Mike reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
