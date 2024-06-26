jason_age_times_bob_premise = 6
jason_age_times_bob_hypothesis = 4

# the hypothesis refers to the age relation between Jason and Bob, mentioned also in the premise
if jason_age_times_bob_hypothesis >= jason_age_times_bob_premise:
    # check if 'jason_age_times_bob_hypothesis' contradicts the premise that Jason is less than 'jason_age_times_bob_premise' times older than Bob
    label = "contradiction"
elif jason_age_times_bob_hypothesis < jason_age_times_bob_premise:
    # if 'jason_age_times_bob_hypothesis' is less than 'jason_age_times_bob_premise' then it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
