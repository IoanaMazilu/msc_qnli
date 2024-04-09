suresh_efficiency_premise = 25
suresh_efficiency_hypothesis = 35

# the hypothesis refers to the efficiency of Suresh compared to Kamal, as mentioned in the premise
if suresh_efficiency_premise > suresh_efficiency_hypothesis:
    # check if the efficiency percentage in the premise contradicts the hypothesis
    label = "contradiction"
elif suresh_efficiency_premise < suresh_efficiency_hypothesis:
    # check if the efficiency percentage in the premise is less than the hypothesis
    label = "entailment"
else:
    # if the efficiency percentages are equal, we can infer neutrality
    label = "neutral"

print(label)
