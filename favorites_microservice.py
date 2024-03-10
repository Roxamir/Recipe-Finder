while True:
    with open("fav_cmd.txt", 'r') as file:
        cmd = file.readline()
        
        if cmd == "ADD":
            