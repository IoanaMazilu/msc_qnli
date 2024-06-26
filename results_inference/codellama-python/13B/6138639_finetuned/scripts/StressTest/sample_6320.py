apples_maddie_premise = 4
apples_maddie_hypothesis = 6
apples_given = 2

# the hypothesis talks about the number of apples Maddie has, referenced also in the premise
if apples_maddie_hypothesis!= apples_maddie_premise:
    # check if the number of apples in the hypothesis contradicts the number of apples reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)