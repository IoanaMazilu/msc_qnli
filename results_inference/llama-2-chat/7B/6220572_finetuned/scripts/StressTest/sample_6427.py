less_than_premise = 750
sold_to_george_premise = 450
sold_to_george_hypothesis = 450

# the hypothesis talks about the number of cookies sold to George, referenced also in the premise
if sold_to_george_hypothesis <= less_than_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_premise'
    label = "contradiction"
elif sold_to_george_hypothesis!= sold_to_george_premise:
    # check if the number of sold cookies in the hypothesis contradicts the number of sold cookies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
