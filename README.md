# wechat-reminder
⛩ A simple tool that sends remind to WeChat from command-line.

## Usage
Just type `wechat-reminder` with arguments in the command line. Argument `title` is required.
```bash
$ wechat-reminder -h
usage: wechat-reminder_main.py [-h] --title TITLE [--desp DESP]

Send a message to WeChat.

optional arguments:
  -h, --help     show this help message and exit
  --title TITLE  Title of the message. The maximum length is 32.
  --desp DESP    Description of the message. The maximum length is 32KB.
```

You can run the tool after any long-running command like deep learning experiments, so that WeChat will be notified when the command finishes running normally.
```bash
sleep 3 && wechat-reminder --title "hello" --desp "Remind after 3 seconds"
```

## Install
Run the following command, and follow the on-screen instructions.
```bash
bash <(curl -s https://raw.githubusercontent.com/magic3007/wechat-reminder/master/install.sh)
```
wechat-reminder is implemented using python. So you should have a python3 interpreter and install the required python package.
```bash
pip install -r requirements.txt
```
Request a key from [server酱](https://sct.ftqq.com/), and export it as an environment variable `FT_SCKEY`:
```bash
export FT_SCKEY=xxx
```
