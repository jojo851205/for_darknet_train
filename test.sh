#!/bin/bash
# Program: to check darknet can train successfully
# 2020/11/23

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#read -p "Please input a directory: " dir
input_dir="new_tooth"

echo  $input_dir

if [ -d "./$input_dir" ]; then
    # 目錄 darknet/new_tooth 存在
    echo $input_dir "Exist."
else
    # 目錄 darknet/new_tooth 不存在
    echo $input_dir " NOT exist."
fi

# End if any error occur
set -e

#檔案數量是否正確
python count_data.py $input_dir 
echo "count_data.py finish"
#images 位置
python jpg_addr.py $input_dir 
echo "jpg_addr.py finish"
#執行訓練
./darknet detector train $input_dir/cfg/obj.data $input_dir/cfg/yolov3.cfg
#多GPU訓練
./darknet detector train $input_dir/cfg/obj.data $input_dir/cfg/yolov3.cfg $input_dir/cfg/yolov3_last.weights -gpus 0,1 
echo "training finish"
#訓練完weight整理
mv $input_dir/cfg/yolov3_last.weights $input_dir/cfg/yolov3_selected.weights
#刪除不重要的weights
find $input_dir/cfg/ -type f | grep 0.weights | xargs rm 
echo "Clean weights!  "

#訓練檔案改成訓練完成日期
date=`date +%Y%m%d -d " 1 days ago " `
echo $date
mv $input_dir $date

echo "NEW Training dir : $date "

#訓練資料夾重建
mkdir $input_dir
cp -r $date/cfg $input_dir/cfg
echo "rebuild train_dir "
find $input_dir/cfg/ -type f | grep weights | xargs  rm
echo "Clean weights ! "
find $input_dir/cfg/ -type f | grep txt | xargs  rm  
echo "Clean txt ! "
cp $date/cfg/yolov3_selected.weights $input_dir/cfg/
mkdir $input_dir/images
#訓練weights 搬家
echo "rebuild train_dir finish "

output_dir="test_results/new_tooth/disease"

cp -r $date/cfg $output_dir/$date

echo "Backup $date to test_results/new_tooth/disease Finish! "