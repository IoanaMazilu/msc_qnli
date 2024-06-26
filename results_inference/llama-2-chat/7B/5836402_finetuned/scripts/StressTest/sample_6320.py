apples_initial_premise = 4
apples_given_premise = 2
apples_initial_hypothesis = 6
apples_given_hypothesis = 2

# the hypothesis refers to the initial number of apples and the number of apples given, also mentioned in the premise
if apples_initial_hypothesis!= apples_initial_premise:
    # check if the initial number of apples in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
elif apples_given_hypothesis!= apples_given_premise:
    # check if the number of apples given in the hypothesis contradicts the number of apples given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
