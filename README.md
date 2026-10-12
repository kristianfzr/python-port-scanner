# Python Port Scanner
This is a simple port scanner built in python (one file) and scans either all ports or only the ones you provide in a list.

### Example usage:

Ports from 1 to 65535:
```
python app.py www.dir.bg
```

Specific ports:
```
python app.py www.dir.bg --ports 80 443 3389 22
```