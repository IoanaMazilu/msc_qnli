# Premise: After the deal closes, Teva will generate sales of about $7 billion a year, the company said.
# Hypothesis: Teva earns $7 billion a year.
# Golden Label: neutral

sales_premise = 7e9
sales_hypothesis = 7e9

# the hypothesis talks about the sales of Teva, which is also mentioned in the premise
# but the premise mentions this as a future event ("After the deal closes"), while the hypothesis states it as a current fact
# as the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise, we infer neutral
label = "neutral"

print(label)

