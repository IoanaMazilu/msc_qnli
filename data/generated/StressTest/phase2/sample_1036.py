# Premise: Lionel left his house and walked towards Walt's house, less than 58 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, 48 miles away.
# Golden Label: neutral

distance_to_walt_premise = 58
distance_to_walt_hypothesis = 48

# the hypothesis talks about the distance Lionel walked towards Walt's house, which is also mentioned in the premise
if distance_to_walt_hypothesis > distance_to_walt_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_to_walt_premise' 
    label = "contradiction"
elif distance_to_walt_hypothesis < distance_to_walt_premise:
    # any distance less than 'distance_to_walt_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value equals the premise's upper limit, we can infer entailment
    label = "entailment"

print(label)

