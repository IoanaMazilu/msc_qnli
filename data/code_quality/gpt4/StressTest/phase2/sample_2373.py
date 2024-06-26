people_premise = 12
people_hypothesis = 42

# the hypothesis talks about the number of people in a BCCI meeting which is also mentioned in the premise
if people_premise > people_hypothesis:
    # check if the number of people in the premise contradicts the estimate of less than 'people_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
