# Premise: Beamon's jump was a world record that eclipsed the previous record by 21 3/4 inches. The jump still stands as an Olympic record, and stood as a world record until Mike Powell leapt 29'4 1/2'' at the 1991 World Championships in Tokyo.
# Hypothesis: 2,45 m is the world record in the high jump.
# Golden Label: neutral

beamon_jump_inches_record_increase = 21 + 3/4
powell_jump_inches_record = 29 * 12 + 4 + 1/2 # convert feet to inches
high_jump_record_meters_hypothesis = 2.45

# the hypothesis talks about the world record in high jump, whereas the premise is about long jump records
# the high jump record is not mentioned in the premise
label = "neutral"

print(label)

