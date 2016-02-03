# kamebot
- python3
- printで出力したものをファイルとしてSlackに投げる 

## How to install 
```
pip install git+https://github.com/masaponto/kame_bot
```

## Examples

Write hoge.py as follows

```python
from kame_bot import KameBot

bot = KameBot('<your-slack-api-token-goes-here>',channel='#random')

@bot.toslack
def hoge():
    print('this is a test')

if __name__ == "__main__":
    hoge()
```

then Run

```
python hoge.py out.txt
```
