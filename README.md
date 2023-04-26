# install package
```
pip install mindmate
```

> It's not recommended to install in virtual environment _(except for  testing)_ try it with default `pip`
# usage
```
$ mindmate [ARGUMENT] [OPTIONS] [OPTIONS] [OPTIONS] --help
```

# examples
```
$ mindmate configure
$ mindmate ai prompting list

$ mindmate chat -P openai \
  -m text-davinci-003 \
  -p "Act as a professional developer, provide best file structure for openAPI framework"
```

# compatibility

__Not tested__ yet, but should be compatible with any Python > 3.8