group_premise = "United States"
group_hypothesis = "Slovenia"

# compare the names of the teams in the premise and hypothesis
if group_premise!= group_hypothesis:
    # if the names of the teams contradict, label the answer as "contradiction"
    label = "contradiction"
else:
    # if the names of the teams match, continue to compare other aspects of the premise and hypothesis
    pass

# compare the score in the premise and hypothesis
if premise.score!= hypothesis.score:
    # if the scores contradict, label the answer as "contradiction"
    label = "contradiction"
else:
    # if the scores match, continue to compare other aspects of the premise and hypothesis
    pass

# if no contradiction is found, label the answer as "entailment"
label = "entailment"

print(label)
