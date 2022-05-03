"# fast-click" 



Command  Speed
python cli.py  0.3
fast-click  0.3


# Time the importtime
`python -X importtime fast_click.py`


# Visualize
```bash
pip install tuna
python -X importtime yourfile.py 2> import.log
tuna program.prof
```

# Slow Anyconfig
```py
import anyconfig
anyconfig.load

## partial import
from anyconfig import load

# Summary
1. Avoid pkg_source load - pip install from wheel
2. Slow dynaconf / anyconfig
3. Lazy Loading