#!/bin/bash
# File              : install-gitee.sh
# Author            : Jing Mai <jingmai@pku.edu.cn>
# Date              : 05.25.2022
# Last Modified Date: 2026-02-13
# Last Modified By  : Created for Gitee mirror
#
# 专为 Gitee 镜像仓库设计的安装脚本
# Gitee 镜像地址：https://gitee.com/magic3007/wechat-reminder

server=https://gitee.com/magic3007/wechat-reminder/raw/master
local=$HOME/.wechat-reminder

echo "Will install wechat-reminder from Gitee mirror to $HOME/.wechat-reminder"
read -p "Proceed? (y/n)" -n 1 -r
echo

if ! [[ $REPLY =~ ^[Yy]$ ]]; then
    exit
fi


mkdir -p $local

for filename in wechat-reminder wechat-reminder_main.py LICENSE requirements.txt; do
    echo "Downloading $filename"
    curl -s $server/$filename --output $local/$filename
done

chmod +x $local/wechat-reminder*

if [[ ":$PATH:" == *":$HOME/.local/bin:"* ]]; then
    echo "Putting wechat-reminder executable to $HOME/.local/bin."
    ln -fs $local/wechat-reminder $HOME/.local/bin
    echo "Done."
    exit
fi

if [[ ":$PATH:" == *":$HOME/bin:"* ]]; then
    echo "Putting wechat-reminder executable to $HOME/bin."
    ln -fs $local/wechat-reminder $HOME/bin
    echo "Done."
    exit
fi

read -p "Add wechat-reminder executable to ~/.local/bin? (y/n)" -n 1 -r
echo

if ! [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "You can manually add $local/wechat-reminder to your path later."
    exit
fi

mkdir -p $HOME/.local/bin
ln -fs $local/wechat-reminder $HOME/.local/bin
echo "Done. Please add the following line to your .bashrc, and then relogin to use wechat-reminder:"
echo ""
echo "export PATH=\"$PATH:$HOME/.local/bin\""
echo ""
echo "Note: Remember to install Python dependencies:"
echo "  pip install -r $local/requirements.txt"