def checkID(inPutID):
    
    if len(str(inPutID)) != 4:
        return False
    else:
        try:
            int(inPutID)
        except ValueError:
            return False
    
    return True