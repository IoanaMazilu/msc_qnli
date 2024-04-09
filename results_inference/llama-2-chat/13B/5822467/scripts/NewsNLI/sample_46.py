deaths_premise = 1
injuries_premise = 10
death_hypothesis = 1
wounded_hypothesis = 10

# the hypothesis mentions the number of death and wounded in Al Sanameen, which is also mentioned in the premise
# however, the premise does not provide any information about the location of the incidents
# thus, we cannot infer entailment, contradiction, or neutrality
label = "neutral"

print(label)
