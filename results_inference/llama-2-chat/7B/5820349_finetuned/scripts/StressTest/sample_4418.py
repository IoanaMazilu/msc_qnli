average_increase_premise = 2
average_increase_hypothesis = 5

# the hypothesis talks about the points Jerry wants to raise his average by, referenced also in the premise
if average_increase_hypothesis!= average_increase_premise:
    # check if the points Jerry wants to raise his average by in the hypothesis contradicts the points in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
