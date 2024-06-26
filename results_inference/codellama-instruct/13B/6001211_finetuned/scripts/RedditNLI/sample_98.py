assets_shrinkage_premise = 1.0
assets_fall_hypothesis = 6 # in billion dollars

# the premise and hypothesis mention the net foreign assets of the Saudi central bank
# however, the premise gives the assets shrinkage in percentage while the hypothesis gives it in billion dollars
# we cannot directly compare these two values, so the relation is neutral
label = "neutral"

print(label)
