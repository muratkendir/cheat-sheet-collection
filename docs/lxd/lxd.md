# LXD and LXC Notes

## How to forward a port from instance to the host:

In the example below, "pgpp" is containers name. "postgres-forward" is the name of the rule (device)

```bash
lxc config device add pgpp postgres-forward proxy listen=tcp:0.0.0.0:5432 connect=tcp:127.0.0.1:5432
```

If you want to add port forwarding within a profile, check [this website](https://lxdware.com/forwarding-host-ports-to-lxd-instances/)
