injured_premise = 6
injured_hypothesis = 6
seriously_injured_premise = 4
seriously_injured_hypothesis = 0

# the hypothesis mentions the number of injured people, which is also mentioned in the premise
# however, the hypothesis does not mention the number of seriously injured people, which is mentioned in the premise
if seriously_injured_hypothesis!= seriously_injured_premise:
    # check if the number of seriously injured people from the hypothesis contradicts the number of seriously injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
