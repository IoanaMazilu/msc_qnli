museum_visitors = 100
art_gallery_visitors = 50

# the hypothesis talks about the number of visitors to the museum and art gallery
if museum_visitors <= art_gallery_visitors:
    # check if the hypothesis value contradicts the estimate of more than 'art_gallery_visitors'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of visitors to the art gallery
    # any number of visitors greater than 'art_gallery_visitors' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
