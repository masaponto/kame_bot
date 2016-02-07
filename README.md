# kamebot :turtle:
- Python3
- using [slacker](https://github.com/os/slacker)
- printで出力したものをSlackに投げる 



## How to install 
1. Install via pip  
   ```
   $ pip install git+https://github.com/masaponto/kamebot  
   ```
2. Add KAMEBOT_TOKEN to your shell  
   ```
   $ echo 'export KAMEBOT_TOKEN = <your-slack-api-token-goes-here>' >> ~/.zshenv
   ```

## Examples

Write example.py as follows  

```python
from kamebot import Kamebot

kame = Kamebot(channel='#random')

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

kame = Kamebot(channel='#random')

# send print string as a file
@kame.afile
def main():
    print('this is a test')

if __name__ == "__main__":
    main()
```

then Run  
```
$ python example.py your_output_file.txt
```
