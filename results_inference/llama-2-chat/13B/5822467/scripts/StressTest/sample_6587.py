sony_johnny_catch_premise = 60
sony_johnny_catch_hypothesis = 30

# the hypothesis refers to the number of fish caught by Sony and Johnny
if sony_johnny_catch_premise <= sony_johnny_catch_hypothesis:
    # check if the estimate of'sony_johnny_catch_hypothesis' contradicts the number of fish caught in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fish caught
    # any number of fish caught less than or equal to 30 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
