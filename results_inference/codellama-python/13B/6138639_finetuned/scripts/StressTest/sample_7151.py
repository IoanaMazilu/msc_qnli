chiefs_premise = 5
chiefs_hypothesis = 1

# the hypothesis talks about the number of joint chiefs of staff at a meeting, referenced also in the premise
if chiefs_hypothesis!= chiefs_premise:
    # check if the number of joint chiefs in the hypothesis contradicts the number of joint chiefs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
