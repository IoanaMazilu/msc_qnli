y_entailment = 0
y_contradiction = 0
y_neutral = 1

# the hypothesis talks about the number of fish Lilly and Rosy have, which is also mentioned in the premise
if rosy_fish_premise > rosy_fish_hypothesis:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    y_contradiction = 1
elif rosy_fish_hypothesis > rosy_fish_premise:
    # check if the number of fish Rosy has in the hypothesis contradicts the number of fish Rosy has in the premise
    y_contradiction = 1
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    y_entailment = 1

print(y_entailment)
print(y_contradiction)
print(y_neutral)
