fish_from_farms_premise = 0.7
fish_from_farms_hypothesis = 0.7

# the hypothesis mentions the percentage of fish from fish farms that goes to markets, which is also referenced in the premise
# however, the premise specifies the information for Aberdeen market only, while the hypothesis generalizes for local wholesale markets
# thus, we cannot fully entail the hypothesis from the premise
label = "neutral"

print(label)
