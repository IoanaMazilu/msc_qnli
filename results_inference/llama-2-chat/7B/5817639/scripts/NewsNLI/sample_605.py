deaths_premise = 29
deaths_hypothesis = 35

# the hypothesis mentions a higher number of deaths in Marion County than the premise
if deaths_hypothesis!= deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
