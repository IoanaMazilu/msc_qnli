infected_premise = 100000
infected_hypothesis = 100000

# the hypothesis mentions the number of infected people in China, which is also mentioned in the premise
# however, the hypothesis does not explicitly state that the number of infected people in China is greater than 100,000
# therefore, we can infer entailment
label = "entailment"

print(label)
