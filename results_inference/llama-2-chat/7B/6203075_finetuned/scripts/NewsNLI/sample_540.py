concerned_americans_premise = 1/3
not_worried_americans_premise = 69
worrying_americans_hypothesis = 52

# the hypothesis mentions the percentage of Americans who worry about a bridge collapsing
# the premise gives the percentage of Americans who are concerned and not worried
if worrying_americans_hypothesis!= concerned_americans_premise:
    # check if the percentage of Americans who worry in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
elif not_worried_americans_premise >= 69:
    # check if the percentage of Americans who are not worried in the premise contradicts the percentage in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
