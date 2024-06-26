detained_premise = 939
arrested_hypothesis = 939

# the hypothesis mentions the number of people arrested in Turkey, which is also mentioned in the premise
# however, the premise refers to people detained in connection with protests, while the hypothesis does not specify the reason for arrest
if detained_premise != arrested_hypothesis:
    # check if the number of people arrested in the hypothesis contradicts the number of people detained reported in the premise
    label = "contradiction"
else:
    # if the number of people arrested does not contradict the number of people detained, we infer neutrality as the context of arrest is not specified in the hypothesis
    label = "neutral"

print(label)
