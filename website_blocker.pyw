import time
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com" , "facebook.com", "www.primevideo.com","www.wattpad.com", "www.amazon.com", "www.amazon.in","primevideo.com"]
weekdays = [0, 1, 2, 3, 4, 5]
work_hours = [  8, 9, 10, 11, 12, 13, 14 ,15, 16, 20, 21,22,23,0,1,2,3]

#flag = True

while True:
    time_right_now = time.localtime()
    if ((time_right_now.tm_wday in weekdays) and(time_right_now.tm_hour in work_hours)):

        print("Working hours")
        with open(host_path, 'r+' ) as myfile:
            content = myfile.read()
        print(content)
        print("\n")

        for x in websites:
            if x in content:
                pass
            else:
                with open(host_path, 'a+') as myfile:
                    myfile.write(redirect+"\t"+x+"\n")

    else:
        #flag = False
        with open(actual_host_content, "r") as host_content :
            host_contains = host_content.read()

        with open(host_path, 'w') as file:
            file.write(host_contains)
        print("Fun Hours")

    time.sleep(60 * 5)



