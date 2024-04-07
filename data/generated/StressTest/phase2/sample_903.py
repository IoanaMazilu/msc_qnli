# Premise: Mike can catch 30 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Hypothesis: Mike can catch less than 60 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Golden Label: entailment

mike_fish_premise = 30
mike_fish_hypothesis = 60
jim_fish_premise = mike_fish_premise * 2
bob_fish_premise = jim_fish_premise * 1.5

jim_fish_hypothesis = mike_fish_hypothesis * 2
bob_fish_hypothesis = jim_fish_hypothesis * 1.5

# the hypothesis talks about the number of fish Mike, Jim and Bob can catch in an hour, referenced also in the premise
if mike_fish_hypothesis >= mike_fish_premise:
    # check if the hypothesis value contradicts the premise value for Mike
    label = "contradiction"
elif jim_fish_hypothesis != jim_fish_premise:
    # check if the hypothesis value contradicts the premise value for Jim
    label = "contradiction"
elif bob_fish_hypothesis != bob_fish_premise:
    # check if the hypothesis value contradicts the premise value for Bob
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

