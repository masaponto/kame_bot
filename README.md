# kame_bot
- python3
- printで出力したものをファイルとしてSlackに投げる 

## How to install 
```
pip install git+
```

## example

```python:example.py
bot = KameBot('<your-slack-api-token-goes-here>',channel='#random')

@bot.toslack
def hoge():
    print('this is a test')

if __name__ == "__main__":
    hoge()
```
