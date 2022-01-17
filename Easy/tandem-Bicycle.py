
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    totalSpeed = 0
    fastest = False
    if fastest == True:
        totalSpeed = min(redShirtSpeeds) + max(blueShirtSpeeds)
    else:
        totalSpeed = max(redShirtSpeeds) + max(blueShirtSpeeds)

    return totalSpeed


redShirtSpeeds = [1,2,3,4]
blueShirtSpeeds = [4,3,2,1]
fastest=True
print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest))
