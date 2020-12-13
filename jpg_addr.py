# -*- coding:utf-8 -*-
import os
import sys
import traceback
import random
  


if __name__ == "__main__":

    try:
        Date = sys.argv[1]
        Train_data = os.path.join(Date, "images")
        Train_data_txt = os.path.join(Date, "cfg/train.txt")
        Val_data_txt = os.path.join(Date, "cfg/valid.txt")
        path = os.listdir(Train_data)
        jpg_files = 0
        f = open(Train_data_txt,'a')
        list = []
        for fn in path:
                #print (fn)                
                if ".jpg" in fn:
                    jpg_files += 1
                    #print(jpg_files)
                    line = Train_data+'/'+fn+'\n'
                    f.write(line)
                    list.append(line)
        f.close()
        print ("Train_data : " + str(jpg_files))
        print ("train.txt OK! ")

        g =  open(Val_data_txt, 'a',)
        val_files =  int(jpg_files*0.2)
        a = random.sample(list,val_files)
        for i in a:
            g.write(i)
        g.close()
        print ("Val_data : "+ str(val_files))
        print ("valid.txt OK ")

    except:
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)       