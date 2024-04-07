# Premise: If Suresh is 25% more efficient than Kamal, he can complete the work in---days.
# Hypothesis: If Suresh is less than 65% more efficient than Kamal, he can complete the work in---days.
# Golden Label: entailment

suresh_efficiency_premise = 25
suresh_efficiency_hypothesis = 65

# the hypothesis refers to the efficiency of Suresh compared to Kamal as mentioned in the premise
if suresh_efficiency_premise >= suresh_efficiency_hypothesis:
    # check if the 'suresh_efficiency_premise' contradicts the hypothesis which states Suresh is less than 65% more efficient
    label = "contradiction"
elif suresh_efficiency_premise < suresh_efficiency_hypothesis:
    # check if the 'suresh_efficiency_premise' can explicitly entail the hypothesis which states Suresh is less than 65% more efficient
    label = "entailment"
else:
    # if the premise efficiency of Suresh cannot contradict or entail the hypothesis, we infer neutrality
    label = "neutral"

print(label)

