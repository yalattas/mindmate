# install package

## virtual environment
```
pip install mindmate
```
> It's not recommended to install in virtual environment _(except for  testing)_ try it with default `pip`

## operating system level
```
sudo apt update
sudo apt install -y python3-pip
export PATH="$PATH:/home/<USER>/.local/bin"
pip install mindmate
```
# usage
```
$ mindmate [ARGUMENT] [OPTIONS] [OPTIONS] [OPTIONS] --help
```

## examples
```
$ mindmate configure
$ mindmate ai prompting list

$ mindmate chat --platform openai \
  --model text-davinci-003 \
  --stream true \
  --max-tokens 500 \
  --prompt "Act as a professional developer, provide best file structure for fastAPI framework"
```

# compatibility

__Not tested__ yet, but should be compatible with any Python >= 3.8
