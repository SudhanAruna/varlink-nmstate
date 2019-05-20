# varlink-nmstate PoC

## Using a dedicated server process:
```shell
yum install python3-varlink python3-libnmstate
python3 varlink-nmstate.py # this blocks, now open a second shell
```

```shell
# get the current network state
python3 varlink-nmstatectl.py unix:./varlink_test get
```

## Creating the server implicitly
```shell
python3 ./varlink-nmstatectl2.py get
```
