import os, time, json 
 from config import banner 
 from multiprocessing import cpu_count 
  
  
 cpu_thread = cpu_count() 
  
  
 def OffMiner(): 
  
     banner() 
     try: 
        print("ตัวอย่าง:") 
        print(" \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m") 
        print(" \033[93mstratum+tcp://verus.asia.mine.zergpool.com:3300\033[00m") 
        pool = input(" pool : ") 
        print("\033[35m-----------------------------------------\033[0m") 
  
        print("ตัวอย่าง: \033[93mRQpWNdNZ4LQ5yHUM3VAVuhUmMMiMuGLUhT\033[00m") 
        wallet = input("wallet: ") 
        print("\033[35m-----------------------------------------\033[0m") 
  
        print("ตัวอย่าง:") 
        print("  \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m") 
        print("  \033[93mc=DOGE,mc=VRSC (ไม่ต้องใส่ id=ชื่อ ระบบจะเพิ่มให้เอง)\033[00m") 
        password = input("password : ") 
  
  
        print("\033[35m-----------------------------------------\033[0m") 
        if pool == "" or wallet == "": 
             raise Exception() 
        if password == "": 
             password = "x"  
        push = { 
             'status': True, 
             'pool': pool, 
             'wallet': wallet, 
             'pass': password 
         } 
     with open("set-miner/online.json", "w") as set: 
         json.dump(push, set, indent=4)   
  
        print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m") 
        name = input("[-n]: ") 
        print("\033[35m-----------------------------------------\033[0m") 
  
        print(f"จำนวนthread \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m") 
        cpu = int(input("[-t]: ")) 
        print("\033[35m-----------------------------------------\033[") 
  
        if name == "": 
             raise Exception() 
        if cpu == "": 
             cpu = 1 
     except: 
             os.system("@cls||clear") 
             time.sleep(3) 
             print("เกิดข้อผิดพลาด") 
             os.system("edit-miner") 
  
         push = { 
                  'status': True, 
                  'name': name, 
                  'cpu': cpu 
             } 
         with open("set-miner/offline.json", "w") as set: 
              json.dump(push, set, indent=4) 
  
  
 while True: 
     banner() 
     OffMiner()            
     break
