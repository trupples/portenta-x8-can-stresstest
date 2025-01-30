Run `sudo ./can_setup.sh` on the host (outside of the container) to reset and configure the can1 interface. Do this once at the beginning, and re-run if the interface gets stuck.

Build container:
```
docker build -t can_stresstest .
```

Run candump and start sending regular messages:
```
docker run --network host -it can_stresstest bash -c 'candump can1 & python3 can_basic.py 123'
```

If running multiple instances (possibly on multiple machines), you may change the `123` to be able to distinguish between frames sent by each instance.

