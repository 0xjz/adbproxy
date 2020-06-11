# adbproxy
set android proxy setting to point my machine via adb shell. 

```
Example
$ ./adbproxy.py
interface   --> "en0"
ip addr     --> "10.10.1.3"
proxy port  --> "8080"
done.
```

```
Usage
$ ./adbproxy.py 
$ ./adbproxy.py en0
$ ./adbproxy.py eth0 8080
```
