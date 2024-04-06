# Premise: Saudi central bank net foreign assets fall $6 billion in March.
# Hypothesis: Saudi central bank net foreign assets shrink 1.0 pct in March.
# Golden Label: neutral

assets_fall_premise = 6 # in billion dollars
assets_fall_hypothesis = 1.0 # in percentage

# The hypothesis and premise mention the fall of net foreign assets of the Saudi central bank in March.
# However, the premise gives the fall in billion dollars while the hypothesis gives it in percentage.
# We cannot infer the fall in percentage from the fall in billion dollars nor vice versa.
label = "neutral"

print(label)

