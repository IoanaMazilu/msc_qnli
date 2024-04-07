# Premise: Shridhar together earned 19800.
# Hypothesis: Shridhar together earned less than 79800.
# Golden Label: entailment

earnings_premise = 19800
earnings_hypothesis = 79800

# the hypothesis is about the earnings of Shridhar, which is also mentioned in the premise
if earnings_premise > earnings_hypothesis:
    # check if the actual earnings of Shridhar contradicts the upper limit estimate given in the hypothesis
    label = "contradiction"
elif earnings_premise == earnings_hypothesis:
    # check if the actual earnings of Shridhar contradicts the 'less than' condition in the hypothesis
    label = "contradiction"
else:
    # if the actual earnings do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

