#!/bin/bash
# 批量翻译脚本

download_list="download_list.txt"
source_dir="_source/docs"

# 定义翻译映射（简单的日文到中文）
declare -A translations

# 读取下载列表
total=$(wc -l < "$download_list")
current=0

while IFS=$'\t' read -r name href md_path; do
    if [ -z "$name" ]; then
        continue
    fi
    
    current=$((current + 1))
    echo "[$current/$total] 处理: $name"
    echo "  文件: $md_path"
    
    # 检查HTML文件是否存在
    html_file="/tmp/temph/$(basename $href)"
    if [ ! -f "$html_file" ]; then
        echo "  [下载中...]"
        curl -s --connect-timeout 30 "http://beginners.biz/$href" -o "$html_file"
        if [ $? -eq 0 ]; then
            echo "  [下载成功]"
        else
            echo "  [下载失败]"
            continue
        fi
    fi
    
    # 延迟
    sleep 1
done < "$download_list"

echo "批量处理完成"
