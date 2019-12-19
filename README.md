# telnet-serial-adapter
This tool provide a way to use telnet to access devices which does have public network interface


# Topology


DUT---------(serial console)------PC--------(telnet)--------Test Station

When DUT does not provide the public network interface, and the Test Station can not connect to the DUT via serial console directly. We can run this tool on a PC to solve this problem
