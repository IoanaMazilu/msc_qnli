sanket_finish_time_premise = 35
sanket_finish_time_hypothesis = 15

# the hypothesis talks about the time Sanket finishes the race, referenced also in the premise
if sanket_finish_time_hypothesis >= sanket_finish_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sanket_finish_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Sanket's finish time
    # any finish time less than 'sanket_finish_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)