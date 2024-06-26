yt_viewed_premise = 1.2 million
yt_viewed_hypothesis = 1.2 million

# the hypothesis mentions the number of people who have viewed the video on YouTube, which is also mentioned in the premise
# however, the hypothesis does not provide any additional information about the video's views

if yt_viewed_hypothesis <= yt_viewed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'yt_viewed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of views
    # any number of views greater than 'yt_viewed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
