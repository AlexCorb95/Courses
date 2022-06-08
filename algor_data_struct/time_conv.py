def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:-2]
    elif s[-2:] == "AM":
        return s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    else:
       int_s= int(s[:2]) + 12
       return str(str(int_s) + s[2:8])


s="12:05:45AM"
print(timeConversion(s))