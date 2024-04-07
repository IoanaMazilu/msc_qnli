# Premise: If 41 people have visited both Iceland and Norway, how many people have visited neither country?
# Hypothesis: If 11 people have visited both Iceland and Norway, how many people have visited neither country?
# Golden Label: contradiction

visited_both_premise = 41
visited_both_hypothesis = 11

# the hypothesis talks about the number of people who visited both countries, referenced also in the premise
if visited_both_hypothesis != visited_both_premise:
    # check if the hypothesis value contradicts the value of 'visited_both_premise'
    label = "contradiction"
else:
    # we do not have enough information to infer either entailment or neutrality. 
    label = "neutral"

print(label)
