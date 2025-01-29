#MPIN DETECTION : WEAK OR STRONG

#Solution Code for 4-Digit MPIN for 20 test cases

def check_weak(mpin, reason):
    vec = [int(digit) for digit in mpin]
    
    if vec[0] == vec[1] or vec[2] == vec[3]:
        reason.append("COMMONLY_USED")
    if vec[0] == vec[2] and vec[1] == vec[3]:
        reason.append("COMMONLY_USED")
    if vec[0] + 1 == vec[1] and vec[1] + 1 == vec[2] and vec[2] + 1 == vec[3]:
        reason.append("COMMONLY_USED")

def check_date(dob, mpin_segments):
    date_parts = [dob[i:i+2] for i in range(0, len(dob), 3) if dob[i:i+2] != '-']
    
    for segment in mpin_segments:
        if segment in date_parts:
            return True
    return False

def test_mpin_strength():
    test_cases = [
        {"mpin": "1234", "dob": "12-03-1999", "spouse_dob": "15-05-1997", "anniversary": "20-10-2018"},
        {"mpin": "5678", "dob": "06-12-1995", "spouse_dob": "07-07-1992", "anniversary": "05-09-2020"},
        {"mpin": "1111", "dob": "11-11-2000", "spouse_dob": "12-12-1998", "anniversary": "01-01-2021"},
        {"mpin": "2345", "dob": "25-06-1989", "spouse_dob": "10-05-1990", "anniversary": "15-08-2015"},
        {"mpin": "8888", "dob": "18-12-1991", "spouse_dob": "19-09-1993", "anniversary": "30-12-2017"},
        {"mpin": "9988", "dob": "01-01-1999", "spouse_dob": "05-03-1998", "anniversary": "12-12-2010"},
        {"mpin": "1212", "dob": "15-04-1995", "spouse_dob": "23-09-1992", "anniversary": "11-11-2011"},
        {"mpin": "5656", "dob": "16-06-2001", "spouse_dob": "17-07-2000", "anniversary": "19-02-2019"},
        {"mpin": "7890", "dob": "02-09-1993", "spouse_dob": "03-10-1991", "anniversary": "07-12-2016"},
        {"mpin": "4567", "dob": "04-04-1994", "spouse_dob": "09-09-1992", "anniversary": "12-11-2014"},
        {"mpin": "9090", "dob": "23-08-1997", "spouse_dob": "01-12-1995", "anniversary": "10-10-2020"},
        {"mpin": "2323", "dob": "12-02-1990", "spouse_dob": "19-03-1993", "anniversary": "24-09-2019"},
        {"mpin": "9999", "dob": "09-09-1999", "spouse_dob": "03-03-2000", "anniversary": "25-12-2022"},
        {"mpin": "4321", "dob": "30-07-1998", "spouse_dob": "15-10-1997", "anniversary": "08-05-2018"},
        {"mpin": "6767", "dob": "07-07-2001", "spouse_dob": "16-06-2000", "anniversary": "13-03-2021"},
        {"mpin": "3030", "dob": "03-03-1993", "spouse_dob": "04-04-1992", "anniversary": "11-11-2017"},
        {"mpin": "4545", "dob": "14-09-1996", "spouse_dob": "21-06-1994", "anniversary": "17-01-2022"},
        {"mpin": "0101", "dob": "15-08-2000", "spouse_dob": "05-05-1998", "anniversary": "02-02-2020"},
        {"mpin": "7070", "dob": "28-02-1997", "spouse_dob": "22-10-1995", "anniversary": "30-06-2023"},
        {"mpin": "3434", "dob": "05-05-1992", "spouse_dob": "18-12-1990", "anniversary": "09-04-2018"}
    ]

    for case in test_cases:
        mpin = case["mpin"]
        dob = case["dob"]
        spouse_dob = case["spouse_dob"]
        anniversary = case["anniversary"]
        
        mpin_segments = [mpin[i:i+2] for i in range(len(mpin) - 1)]
        
        reason = []
        check_weak(mpin, reason)
        
        if check_date(dob, mpin_segments):
            reason.append("DEMOGRAPHIC_DOB_SELF")
        if check_date(spouse_dob, mpin_segments):
            reason.append("DEMOGRAPHIC_DOB_SPOUSE")
        if check_date(anniversary, mpin_segments):
            reason.append("DEMOGRAPHIC_ANNIVERSARY")
        
        if reason:
            print(f"MPIN: {mpin} - STRENGTH : WEAK - {', '.join(reason)}")
        else:
            print(f"MPIN: {mpin} - STRENGTH : STRONG")
        print(f"DOB: {dob}, Spouse DOB: {spouse_dob}, Anniversary: {anniversary}")
        print("-" * 60)

test_mpin_strength()

#Solution Code for 6-Digit MPIN for 20 test cases

def check_weak_six_digit(mpin, reason):
    vec = [int(digit) for digit in mpin]

    if vec[0] == vec[1] or vec[1] == vec[2] or vec[2] == vec[3] or vec[3] == vec[4] or vec[4] == vec[5]:
        reason.append("COMMONLY_USED")

    if (vec[0] == vec[2] and vec[1] == vec[3]) or (vec[2] == vec[4] and vec[3] == vec[5]):
        reason.append("COMMONLY_USED")

    if vec[0] + 1 == vec[1] and vec[1] + 1 == vec[2] and vec[2] + 1 == vec[3] and vec[3] + 1 == vec[4] and vec[4] + 1 == vec[5]:
        reason.append("COMMONLY_USED")

    if vec[0] - 1 == vec[1] and vec[1] - 1 == vec[2] and vec[2] - 1 == vec[3] and vec[3] - 1 == vec[4] and vec[4] - 1 == vec[5]:
        reason.append("COMMONLY_USED")

def check_date(dob, mpin_segments):
    date_parts = [dob[i:i+2] for i in range(0, len(dob), 3) if dob[i:i+2] != '-']
    
    for segment in mpin_segments:
        if segment in date_parts:
            return True
    return False

def test_mpin_strength():
    test_cases = [
        {"mpin": "123456", "dob": "01-01-1980", "spouse_dob": "02-02-1985", "anniversary": "20-10-2018"},
        {"mpin": "654321", "dob": "11-12-1990", "spouse_dob": "21-01-1993", "anniversary": "05-09-2020"},
        {"mpin": "111111", "dob": "22-11-1995", "spouse_dob": "12-12-1998", "anniversary": "01-01-2021"},
        {"mpin": "234567", "dob": "25-06-1989", "spouse_dob": "01-05-1990", "anniversary": "15-08-2015"},
        {"mpin": "888888", "dob": "18-12-1987", "spouse_dob": "19-09-1990", "anniversary": "30-12-2017"},
        {"mpin": "998877", "dob": "05-01-1992", "spouse_dob": "14-03-1995", "anniversary": "12-12-2010"},
        {"mpin": "121212", "dob": "15-04-1985", "spouse_dob": "25-09-1992", "anniversary": "11-11-2011"},
        {"mpin": "565656", "dob": "06-06-2000", "spouse_dob": "07-07-2001", "anniversary": "19-02-2019"},
        {"mpin": "789012", "dob": "09-09-1993", "spouse_dob": "12-11-1991", "anniversary": "07-12-2016"},
        {"mpin": "456789", "dob": "13-04-1994", "spouse_dob": "17-08-1992", "anniversary": "12-11-2014"},
        {"mpin": "909090", "dob": "23-08-1997", "spouse_dob": "30-11-1995", "anniversary": "10-10-2020"},
        {"mpin": "232323", "dob": "18-02-1991", "spouse_dob": "19-03-1993", "anniversary": "24-09-2019"},
        {"mpin": "999999", "dob": "09-09-1999", "spouse_dob": "02-02-2000", "anniversary": "25-12-2022"},
        {"mpin": "432109", "dob": "28-06-1998", "spouse_dob": "12-10-1997", "anniversary": "08-05-2018"},
        {"mpin": "676767", "dob": "07-07-2001", "spouse_dob": "01-01-2000", "anniversary": "13-03-2021"},
        {"mpin": "303030", "dob": "03-03-1992", "spouse_dob": "06-05-1992", "anniversary": "11-11-2017"},
        {"mpin": "454545", "dob": "14-09-1996", "spouse_dob": "01-01-1994", "anniversary": "17-01-2022"},
        {"mpin": "010101", "dob": "22-08-2000", "spouse_dob": "25-12-1998", "anniversary": "02-02-2020"},
        {"mpin": "707070", "dob": "12-05-1997", "spouse_dob": "22-10-1995", "anniversary": "30-06-2023"},
        {"mpin": "343434", "dob": "17-08-1992", "spouse_dob": "28-12-1991", "anniversary": "09-04-2018"}
    ]


    for case in test_cases:
        mpin = case["mpin"]
        dob = case["dob"]
        spouse_dob = case["spouse_dob"]
        anniversary = case["anniversary"]
        
        mpin_segments = [mpin[i:i+2] for i in range(len(mpin) - 1)]
        
        reason = []
        check_weak_six_digit(mpin, reason)
        
        if check_date(dob, mpin_segments):
            reason.append("DEMOGRAPHIC_DOB_SELF")
        if check_date(spouse_dob, mpin_segments):
            reason.append("DEMOGRAPHIC_DOB_SPOUSE")
        if check_date(anniversary, mpin_segments):
            reason.append("DEMOGRAPHIC_ANNIVERSARY")
        
        if reason:
            print(f"MPIN: {mpin} - STRENGTH : WEAK - {', '.join(reason)}")
        else:
            print(f"MPIN: {mpin} - STRENGTH : STRONG")
        print(f"DOB: {dob}, Spouse DOB: {spouse_dob}, Anniversary: {anniversary}")
        print("-" * 60)

test_mpin_strength()

#MPIN DETECTION CODE FOR CUSTOM INPUT

def check_weak_six_digit(mpin, reason):
    vec = [int(digit) for digit in mpin]

    if vec[0] == vec[1] or vec[1] == vec[2] or vec[2] == vec[3] or vec[3] == vec[4] or vec[4] == vec[5]:
        reason.append("COMMONLY_USED")

    if (vec[0] == vec[2] and vec[1] == vec[3]) or (vec[2] == vec[4] and vec[3] == vec[5]):
        reason.append("COMMONLY_USED")

    if vec[0] + 1 == vec[1] and vec[1] + 1 == vec[2] and vec[2] + 1 == vec[3] and vec[3] + 1 == vec[4] and vec[4] + 1 == vec[5]:
        reason.append("COMMONLY_USED")

    if vec[0] - 1 == vec[1] and vec[1] - 1 == vec[2] and vec[2] - 1 == vec[3] and vec[3] - 1 == vec[4] and vec[4] - 1 == vec[5]:
        reason.append("COMMONLY_USED")
        
def check_weak(mpin, reason):
    
    vec = [int(digit) for digit in mpin]
    
    if vec[0] == vec[1] or vec[2] == vec[3]:
        reason.append("COMMONLY_USED")
    if vec[0] == vec[2] and vec[1] == vec[3]:
        reason.append("COMMONLY_USED")
    if vec[0] + 1 == vec[1] and vec[1] + 1 == vec[2] and vec[2] + 1 == vec[3]:
        reason.append("COMMONLY_USED")

def check_date(dob, mpin_segments):
    
    date_parts = [dob[i:i+2] for i in range(0, len(dob), 3) if dob[i:i+2] != '-']
    
    for segment in mpin_segments:
        if segment in date_parts:
            return True
    return False

def main():
    mpin = input("Enter MPIN: ")

    mpin_segments = [mpin[i:i+2] for i in range(len(mpin) - 1)]
    
    reason = []
    if len(mpin) == 4:
        check_weak(mpin, reason)
    else:
        check_weak_six_digit(mpin, reason)
    
    
    dob = input("Enter your DOB (dd-mm-yyyy): ")
    spouse_dob = input("Enter spouse's DOB (dd-mm-yyyy): ")
    anniversary = input("Enter anniversary (dd-mm-yyyy): ")

    if check_date(dob, mpin_segments):
        reason.append("DEMOGRAPHIC_DOB_SELF")
    if check_date(spouse_dob, mpin_segments):
        reason.append("DEMOGRAPHIC_DOB_SPOUSE")
    if check_date(anniversary, mpin_segments):
        reason.append("DEMOGRAPHIC_ANNIVERSARY")

    if reason:
        print("STRENGTH : WEAK -", ', '.join(reason))
    else:
        print("STRENGTH : STRONG")

if __name__ == "__main__":
    main()
