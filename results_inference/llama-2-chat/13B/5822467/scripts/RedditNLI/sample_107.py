premise_time_frame = "two-three weeks"
hypothesis_time_frame = "two weeks"

# define variables with representative names for the numerical entities in both inputs
time_frame_premise = len(premise_time_frame.split(" "))
time_frame_hypothesis = len(hypothesis_time_frame.split(" "))

# extract all quantities as valid numbers (integers or floats)
time_frame_premise_int = int(time_frame_premise)
time_frame_hypothesis_int = int(time_frame_hypothesis)

# compare the time frames
if time_frame_premise_int!= time_frame_hypothesis_int:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
elif time_frame_hypothesis_int > time_frame_premise_int:
    # check if the estimated time frame in the hypothesis is longer than the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the time frame
    # any estimate of the time frame in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
