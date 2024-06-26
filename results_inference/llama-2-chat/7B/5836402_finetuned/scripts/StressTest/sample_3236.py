seniors_premise = 300
seniors_hypothesis = 300

# the hypothesis refers to the number of seniors at Morse High School, which is also mentioned in the premise
if seniors_premise >= seniors_hypothesis:
    # check if the estimate of'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
