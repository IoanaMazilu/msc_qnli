# The hypothesis refers to the number of fish Lilly and Rosy have
# which are also mentioned in the premise
if lilly_fish_premise < 80 and rosy_fish_premise == 8:
    # the hypothesis states Lilly has 10 fish, which is less than 80 fish
    # and Rosy has 8 fish, which is the same as the premise
    label = "entailment"
else:
    # if the hypothesis values contradict the premise ones, we have a contradiction
    label = "contradiction"

print(label)
