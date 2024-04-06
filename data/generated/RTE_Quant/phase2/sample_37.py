# Premise: Indonesia's tin industry is expected to return to profit in 1992 with the dominant state-owned tin mine, Tambang Timah, having cut production costs by 25 per cent since 1990.
# Hypothesis: Indonesia cut tin production costs by 25%.
# Golden Label: neutral

cost_reduction_premise = 25
cost_reduction_hypothesis = 25

# the hypothesis talks about the reduction in tin production costs in Indonesia
# the premise also mentions a 25% reduction in production costs for the state-owned tin mine
# However, it does not explicitly state that the whole of Indonesia's tin industry has had the same cost reduction
# Therefore, we cannot infer entailment, but there is also no contradiction

label = "neutral"

print(label)

