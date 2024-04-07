# Premise: Mike can catch 30 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Hypothesis: Mike can catch more than 30 fish in one hour, Jim can catch twice as much and Bob can catch 50% more than Jim.
# Golden Label: contradiction

mike_fish_premise = 30
mike_fish_hypothesis = 30
jim_fish_premise = mike_fish_premise * 2
jim_fish_hypothesis = mike_fish_hypothesis * 2
bob_fish_premise = jim_fish_premise * 1.5
bob_fish_hypothesis = jim_fish_hypothesis * 1.5

# the hypothesis makes the same claims about the number of fish caught by Jim and Bob as the premise
# but it asserts that Mike can catch more fish than stated in the premise
if mike_fish_hypothesis <= mike_fish_premise:
    # check if the hypothesis value contradicts the number of fish Mike can catch in the premise
    label = "contradiction"
elif jim_fish_hypothesis != jim_fish_premise or bob_fish_hypothesis != bob_fish_premise:
    # check if the number of fish that Jim and Bob can catch in the hypothesis contradicts the number of fish they can catch in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, it still cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

