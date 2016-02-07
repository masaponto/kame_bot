# kamebot :turtle:
- Python3
- using [slacker](https://github.com/os/slacker)
- printで出力したものをSlackに投げる 



## How to install 
1. Install via pip  
```
pip install git+https://github.com/masaponto/kamebot  
```
2. Add KAMEBOT_TOKEN to your shell  
```
$ echo 'export KAMEBOT_TOKEN = <your-slack-api-token-goes-here>' >> ~/.zshenv
```

## Examples

Write hoge.py as follows

```python
from kamebot import Kamebot

kame = Kamebot(channel='#random')

# send print string as a comment
@kame.comment
def hoge():
    print('this is a test')

# send print string as a file
@kame.afile
def fuga():
    print('I am a pen')


if __name__ == "__main__":
    hoge()
    fuga()
```

then Run (out.txt is name of file)
```
$ python hoge.py out.txt
```
