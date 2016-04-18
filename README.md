# kamebot :turtle:
- Python3
- using [slacker](https://github.com/os/slacker)
- printで出力したものをSlackに投げる 
- kamebot自体でargparseを使っているので、[parse_known_args()](http://docs.python.jp/3.5/library/argparse.html#argparse.ArgumentParser.parse_known_args)を使う必要がある  

## How to install 
1. Install via pip  
   ```
   $ pip install git+https://github.com/masaponto/kamebot  
   ```
2. Add KAMEBOT_TOKEN to your shell  
   ```
   $ echo 'export KAMEBOT_TOKEN=<your-slack-api-token-goes-here>' >> ~/.zshenv
   ```  
   slack api token is from [bots](https://slack.com/apps/A0F7YS25R-bots)

## Examples

Write example.py as follows  

```python
from kamebot import Kamebot

kame = Kamebot(channel='#random', error_comment='Yabai!!!!!!!')

# send print string as a comment
@kame.comment
def main():
    print('this is a test')

if __name__ == "__main__":
    main()
```

and Run 
```
$ python example.py
```

if you want send as a file  

```python
from kamebot import Kamebot

kame = Kamebot(channel='#random', error_comment='Yabai!!!!!!!')

# send print string as a file
@kame.afile
def main():
    print('this is a test')

if __name__ == "__main__":
    main()
```

then Run  
```
$ python example.py -of=your_output_file.txt -cm comment
```


## Options
- \-test : if you want to use stdio for test run

##### only for @kame.afile  

- \-cm, \--comment : initial comment for upload file
- \-of, \--outfile : output file name
