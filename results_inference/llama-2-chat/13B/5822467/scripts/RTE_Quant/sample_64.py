victims_premise = 8000 * 100
victims_hypothesis = 800000

# the hypothesis talks about the total number of victims, which is not explicitly mentioned in the premise
# the premise only mentions the average number of victims per day, so we cannot infer entailment or contradiction
label = "neutral"

print(label)
