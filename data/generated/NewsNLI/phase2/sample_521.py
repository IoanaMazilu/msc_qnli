# Premise: Two officials in the Surabaya airport's operations department have been reassigned, said the president director of the state-owned company that manages 13 airports in central and eastern Indonesia.
# Hypothesis: Two officials at Surabaya's airport reassigned, pending investigation.
# Golden Label: neutral

officials_reassigned_premise = 2
officials_reassigned_hypothesis = 2

# the hypothesis mentions the number of officials reassigned in Surabaya's airport, which is also mentioned in the premise
# however, the hypothesis refers to a pending investigation, which cannot be entailed from the premise
label = "neutral"

print(label)

