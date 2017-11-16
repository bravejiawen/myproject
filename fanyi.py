# http://fanyi.baidu.com/?aldtype=16047#zh/en/%E4%BD%A0
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    word = ''.join(sys.argv[1:])
else:
    word = pyperclip.paste()

webbrowser.open('http://fanyi.baidu.com/?aldtype=16047#zh/en/' + word)
