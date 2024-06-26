debentures_premise = 80000
debentures_hypothesis = 10000

# the hypothesis refers to the amount spent on buying debentures, also mentioned in the premise
if debentures_hypothesis >= debentures_premise:
    # check if the hypothesis value contradicts the estimate of less than 'debentures_premise'
    label = "contradiction"
elif debentures_hypothesis < debentures_premise:
    # any amount less than 'debentures_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
