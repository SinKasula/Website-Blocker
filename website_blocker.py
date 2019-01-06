import time
host_path = r"C:\Windows\System32\drivers\etc\hosts" #can be different for os other than windows
redirect = "127.0.0.1"
websites = ["www.facebook.com" , "facebook.com" , "www.wattpad.com", "www.amazon.com", "www.amazon.in"]
weekdays = [0, 1, 2, 3, 4]
work_hours = [5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21]


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
        time.sleep(60 * 5)



