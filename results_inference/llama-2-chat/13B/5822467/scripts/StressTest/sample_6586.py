sony_johnny_catch_premise = 40
sony_johnny_catch_hypothesis = 60

# the hypothesis refers to the number of fish caught by Sony and Johnny
if sony_johnny_catch_premise <= sony_johnny_catch_hypothesis:
    # check if the estimate of'sony_johnny_catch_hypothesis' contradicts the number of fish caught in the premise
    label = "contradiction"
elif sony_johnny_catch_hypothesis > 40:
    # check if the number of fish caught in the hypothesis contradicts the estimate of more than 40 fish caught in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish caught
    # any number of fish greater than 40 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
