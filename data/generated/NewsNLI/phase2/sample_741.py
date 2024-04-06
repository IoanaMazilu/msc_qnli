# Premise: Around 70% -80% of fish sold at Aberdeen fish market already comes from fish farms and aquaculture facilities, mostly around mainland China.
# Hypothesis: Fish farms provide around 70% of fish to local wholesale markets.
# Golden Label: neutral

fish_from_farms_premise = 0.7
fish_from_farms_hypothesis = 0.7

# the hypothesis mentions the percentage of fish from fish farms that goes to markets, which is also referenced in the premise
# however, the premise specifies the information for Aberdeen market only, while the hypothesis generalizes for local wholesale markets
# thus, we cannot fully entail the hypothesis from the premise
label = "neutral"

print(label)

