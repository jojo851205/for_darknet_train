# -*- coding:utf-8 -*-
import os
import sys
import traceback
  


if __name__ == "__main__":

    try:
        Date = sys.argv[1]
        Train_data = os.path.join(Date, "images")
        path = os.listdir(Train_data)
        num_files = 0 #路徑下檔案數量
        jpg_files = 0
        txt_files = 0
        for fn in path:
                num_files += 1
                #print (fn)
                if ".jpg" in fn:
                    jpg_files += 1
                    #print(jpg_files)
                if ".txt" in fn:
                    txt_files += 1
                    #print(txt_files)
        
        print ("All train_data : " +  str(num_files))
        print ("All train_txt_data : " + str(txt_files))
        print ("All train_jpg_data : "+ str(jpg_files))
        if jpg_files > txt_files :
            print("some TXT files are disappeared ")
            sys.exit(1)
        if jpg_files < txt_files :
            print("some IMAGE files are disappeared ")
            sys.exit(1)
        else :
            print(" IMAGE files and TXT files are the same  ")

    except:
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)
        
