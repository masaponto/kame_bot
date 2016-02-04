# kamebot :turtle:
- Python3
- printで出力したものをSlackに投げる 

## How to install 
```
pip install git+https://github.com/masaponto/kamebot
```

## Examples

Write hoge.py as follows

```python
from kamebot import Kamebot

kame = Kamebot('<your-slack-api-token-goes-here>', channel='#random')

# send print string as a comment
@kame.send_comment
def hoge():
    print('this is a test')


# send print string as a file
@kame.send_file
def fuga():
    print('I am a pen')


if __name__ == "__main__":
    hoge()
```

then Run (out.txt is name of file)
```
$ python hoge.py out.txt
```
