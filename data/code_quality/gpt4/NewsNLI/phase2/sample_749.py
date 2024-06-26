co2_cut_premise = 0.20
co2_cut_hypothesis = 0.97

# the hypothesis mentions a significantly higher percentage of CO2 emissions cut than the premise
if co2_cut_hypothesis <= co2_cut_premise:
    # check if the percentage cut in the hypothesis contradicts the percentage cut reported in the premise
    label = "entailment"
elif co2_cut_hypothesis > co2_cut_premise:
    # check if the percentage cut from the hypothesis exceeds the percentage cut in the premise
    label = "contradiction"

print(label)
