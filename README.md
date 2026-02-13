# wechat-reminder
⛩ A simple tool that sends remind to WeChat or Feishu from command-line.

## Usage
Just type `wechat-reminder` with arguments in the command line. Argument `title` is required.

**Note**: The hostname of the machine is automatically prepended to the title in the format `[hostname] title`. This helps identify which machine sent the notification.
```bash
$ wechat-reminder -h
usage: wechat-reminder_main.py [-h] --title TITLE [--desp DESP]

Send a message to WeChat or Feishu.

optional arguments:
  -h, --help     show this help message and exit
  --title TITLE  Title of the message. 
  --desp DESP    Description of the message.
```

You can run the tool after any long-running command like deep learning experiments, so that WeChat will be notified when the command finishes running normally.
```bash
sleep 3 && wechat-reminder --title "hello" --desp "Remind after 3 seconds"
```

## Install
Run the following command, and follow the on-screen instructions.
```bash
bash <(curl -s https://raw.githubusercontent.com/magic3007/wechat-reminder/master/install.sh)
# or
bash <(curl -s https://gitee.com/magic3007/wechat-reminder/raw/master/install-gitee.sh)
```

wechat-reminder is implemented using python. So you should have a python3 interpreter and install the required python package.
```bash
pip install -r requirements.txt
```
Request a key from [pushdeer](https://www.pushdeer.com/), and export it as an environment variable `PUSHDEER_KEY`:
```bash
export PUSHDEER_KEY=xxx
```
You can also add multiple keys splitted by `,`:
```bash
export PUSHDEER_KEY=xxx,xxx,xxx
```

For Feishu (飞书) notifications, follow these steps to get the webhook URL:

### Getting Feishu Webhook URL

1. **Create or select a group** in Feishu where you want to receive notifications
2. **Add a custom bot**:
   - Go to the group settings
   - Select "Group Bots" or "Custom Bots"
   - Click "Add Bot" and choose "Custom Bot"
   - Configure the bot name and description
3. **Get the Webhook URL**:
   - After creating the bot, you'll see a webhook URL
   - URL format: `https://open.feishu.cn/open-apis/bot/v2/hook/{your_token}`
   - Copy this URL
4. **Optional: Configure security settings**:
   - You can enable signature verification for added security
   - If enabled, you'll also get a signing key (currently not supported by this tool)

### Environment Configuration
```bash
# Basic configuration (without signature verification)
export FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/xxx

# Multiple webhook URLs (comma separated)
export FEISHU_WEBHOOK_URL=url1,url2,url3
```

### Notes
- For detailed steps and screenshots, refer to [Feishu Open Platform Documentation](https://open.feishu.cn/document/ukTMukTMukTM/ucTM5YjL3ETO24yNxkjN)
- Signature verification is currently not supported - use webhook URLs without signing verification
- The tool will automatically send notifications to both services if both environment variables are set
