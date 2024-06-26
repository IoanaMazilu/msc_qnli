parties_premise = 25
parties_backing_premise = 20
parties_hypothesis = 1

# the hypothesis mentions the name of the person and his age, which are also mentioned in the premise
# however, the hypothesis does not mention the number of parties backing him, which is mentioned in the premise
if parties_backing_premise > parties_hypothesis:
    # check if the number of parties backing him in the hypothesis contradicts the number of parties backing him in the premise
    label = "contradiction"
else:
    # if the number of parties backing him in the hypothesis does not contradict the number of parties backing him in the premise, we can infer entailment
    label = "entailment"

print(label)
