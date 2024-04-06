# Premise: Police spokesman Maj. Thanassis Kokkalakis added that two suspects arrested in the case are'' domestic terrorists without international connections.''
# Hypothesis: The government names 2 suspects arrested in connection with the bombs.
# Golden Label: neutral

suspects_premise = 2
suspects_hypothesis = 2

# the hypothesis mentions the number of suspects arrested which is also referenced in the premise
# However, the hypothesis does not mention any details about the suspects being "domestic terrorists without international connections" 
# which is stated in the premise. Therefore, the statement from the premise cannot be fully and explicitly entailed from the hypothesis
label = "neutral"

print(label)

