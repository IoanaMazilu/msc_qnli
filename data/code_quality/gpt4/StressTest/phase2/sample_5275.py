messages_premise = 78
messages_hypothesis = 18

# the hypothesis talks about the number of messages Missy might have received from Laurence, referenced also in the premise
if messages_hypothesis >= messages_premise:
    # check if the hypothesis value contradicts the estimate of less than 'messages_premise'
    label = "contradiction"
elif messages_hypothesis < messages_premise:
    # if the number of messages in the hypothesis is less than 'messages_premise', it is consistent with the premise
    # but we cannot explicitly entail it from the premise because the premise uses a general estimate
    label = "neutral"
    
print(label)
