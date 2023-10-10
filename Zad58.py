def main():
    
    temps1 = [] ; temps2 = [] ; temps3 = []
    dates1 = [] ; dates2 = [] ; dates3 = []

    with open("dane_systemy1.txt") as file:
        lines = file.readlines()

        for line in lines:
            date, temp = line.split()

            temps1.append(int(temp, 2))
            dates1.append(int(date, 2))

    with open("dane_systemy2.txt") as file:
        lines = file.readlines()

        for line in lines:
            date, temp = line.split()

            temps2.append(int(temp, 4))
            dates2.append(int(date, 4))

    with open("dane_systemy3.txt") as file:
        lines = file.readlines()

        for line in lines:
            date, temp = line.split()

            temps3.append(int(temp, 8))
            dates3.append(int(date, 8))


          
    min_temp = lowest_temp(temps1, temps2, temps3)
    badtime = bad_time(dates1, dates2, dates3)
    record_days = record_days_counter(temps1, temps2, temps3)



    print(f"S1: {min_temp[0]}, S2: {min_temp[1]}, S3: {min_temp[2]}\n")
    print(f"Bad clock days: {badtime}\n")
    print(f"Record days: {record_days}\n")

    with open("wyniki_systemy.txt", "w") as file:
        file.writelines(f"S1: {min_temp[0]}, S2: {min_temp[1]}, S3: {min_temp[2]}\n")
        file.writelines(f"Suma dni, w ktorych zarejestrowany zegar byl niepoprawny we wszystkich stacjach {badtime}\n")
        file.writelines(f"Liczba dni rekordowych {record_days}\n")


def lowest_temp(temps1, temps2, temps3):
    mintemps = [0, 0, 0]

    for temp1, temp2, temp3 in zip(temps1, temps2, temps3):
        if temp1 < mintemps[0]:
            mintemps[0] = temp1

        if temp2 < mintemps[1]:
            mintemps[1] = temp2

        if temp3 < mintemps[2]:
            mintemps[2] = temp3
        
    return mintemps


def bad_time(dates1, dates2, dates3):
    badtime1 = [] ; badtime2 = [] ; badtime3 = []

    for x in range(len(dates1)):
        time = x*24 + 12
        if dates1[x] != time:
            badtime1.append(x)
    
    for x in range(len(dates2)):
        time = x*24 + 12
        if dates2[x] != time:
            badtime2.append(x)

    for x in range(len(dates3)):
        time = x*24 + 12
        if dates3[x] != time:
            badtime3.append(x)
    
    return common_elements_counter(badtime1, badtime2, badtime3)


def common_elements_counter(list1, list2, list3):
    result = 0
    for element in list1:
        if element in list2:
            if element in list3:
                result += 1
    return result


def record_days_counter(temps1, temps2, temps3):
    counter = 0
    record = [0, 0, 0]

#Cos tu jest zebane, ale nwm co xd
    for temp1, temp2, temp3 in zip(temps1, temps2, temps3):

        if temp1 > record[0]:
            record[0] = temp1
            counter += 1
        
        elif temp2 > record[1]:
            record[1] = temp2
            counter += 1

        elif temp3 > record[2]:
            record[2] = temp3
            counter += 1
    
    return counter




if __name__ == "__main__":
    main()
