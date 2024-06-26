million_people_premise = 1000000
million_people_hypothesis = 1000000

# the premise mentions the number of people in peril, which is also mentioned in the hypothesis
if million_people_premise!= million_people_hypothesis:
    # check if the number of people in peril from the premise contradicts the number of people in peril in the hypothesis
    label = "contradiction"
else:
    # if the premise and the hypothesis values and estimates do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
