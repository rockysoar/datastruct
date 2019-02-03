imaHill = [43, 46, 35, 0, 41, 58, 28, 44, 2, 99, 0, 36, 62, 17, 46, 6, 44, 57, 62, 9, 158, 10]

def climb(startPoint, searchMargin = 5):
    if startPoint >= len(imaHill): return
    startPoint_ = startPoint

    # 前进方向
    smallHill = imaHill[startPoint:min(len(imaHill), startPoint + searchMargin)]
    for k,v in list(enumerate(smallHill)):
        startPoint_ = k+startPoint if v >= imaHill[startPoint_] else startPoint_

    if startPoint_ > startPoint: 
        return climb(startPoint_)
    else:
        return startPoint

startPoint = 2
optimalValue = climb(startPoint)
print('Climbing begin: %d(%d), Possible optimal solution: %d(%d).' % (startPoint, imaHill[startPoint], optimalValue, imaHill[optimalValue]))

