UTC = []
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))
second_of_day = int(input("Second of day:"))

UTC.extend((year, month, day, second_of_day))
print(UTC)

for i in UTC:
    #CHECKING 
    if UTC[0]<=1971:
        print("It can not be convertible, it has to be bigger than 1971")
    if not 1<=UTC[1]<=12:
        print("Month must be integer between 1 and 12")
        break
    if not 1<=(UTC[2])<=31:
        print("Day must be integer between 1 and 31")
        break
    if not 0<=(UTC[3])<=86400:
        print("Second of day must be 0 and 86400")
        break
    
leap_second_epoch = ((30,6,1972) , (31,12,1972) , (31,12,1973) , (31,12,1974) , (31,12,1975) , (31,12,1976) , (31,12,1977) , (31,12,1978) ,
                     (31,12,1979) , (30,6,1981) , (30,6,1982) , (30,6,1983) , (30,6,1985) , (31,12,1987) , (31,12,1989) , (31,12,1990) ,
                     (30,6,1992) , (30,6,1993) , (30,6,1994) , (31,12,1995) , (30,6,1997) , (31,12,1998) , (31,12,2005) , (31,12,2008) ,
                     (30,6,2012) , (30,6,2015) , (31,12,2016))

for i in leap_second_epoch:
    #DETERMINING THE LEAP SECOND VALUE(N)
    if i[2]>=UTC[0] and i[1]>=UTC[1] and i[0]>=UTC[2]:
        N = (leap_second_epoch.index(i))
        UTC[3] += N
        break
    else:
        pass    
    
