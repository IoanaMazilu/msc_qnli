# Premise: 15 years hence, Rohan will be just four times as old as he was 15 years ago.
# Hypothesis: 85 years hence, Rohan will be just four times as old as he was 15 years ago.
# Golden Label: contradiction

years_forward_premise = 15
years_forward_hypothesis = 85
years_backward_premise = 15
years_backward_hypothesis = 15

# the hypothesis talks about the future and past age of Rohan, referenced also in the premise
if years_forward_hypothesis != years_forward_premise:
    # check if the 'years_forward_hypothesis' contradicts the 'years_forward_premise'
    label = "contradiction"
elif years_backward_hypothesis != years_backward_premise:
    # check if the 'years_backward_hypothesis' contradicts the 'years_backward_premise'
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the values in the premise, we cannot infer entailment or contradiction
    label = "neutral"

print(label)

