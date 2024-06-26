apples_maddie_premise = 4
apples_maddie_hypothesis = 7
apples_given = 2

# the hypothesis refers to the number of apples Maddie has, which is also mentioned in the premise
if apples_maddie_premise >= apples_maddie_hypothesis:
    # check if the number of apples Maddie has in the premise contradicts the estimate of less than 'apples_maddie_hypothesis'
    label = "contradiction"
else:
    # if the number of apples Maddie has in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
