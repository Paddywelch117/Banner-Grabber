## Banner-Grabber

A basic Python banner grabbing script to find Open Ports of any hosts and grab banners of services available on different ports.

## Key Features & Benefits

*   **Port Scanning:** Identifies open ports on a specified host.
*   **Banner Grabbing:** Retrieves service banners from open ports, revealing information about running services.
*   **Threaded Scanning:** Implements multi-threading for faster port scanning.



## Prerequisites & Dependencies

*   **Python 3.x:** Ensure Python 3 or later is installed on your system.
*   **socket module:** This is part of the standard Python library and doesn't require separate installation.
*   **threading module:** This is part of the standard Python library and doesn't require separate installation.



## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Paddywelch117/Banner-Grabber.git
    cd Banner-Grabber
    ```

2.  **No specific installation is required.** The script `BannerGrabber.py` is self-contained.



## Usage Examples

1.  **Basic Usage:**

    To run the banner grabber, execute the script:

    ```bash
    python3 BannerGrabber.py
    ```

    **Note:**  The script currently attempts to scan `localhost`.  To scan a different host, modify the `host` variable within `BannerGrabber.py`. Also, no port range is defined so the script will not execute as is, this will need to be added.  An example of that is demonstrated below.

    ```python
    import socket
    import threading
    import time


    def scanner(port):
        try:
            host = "127.0.0.1"  # You can change this to any IP or hostname
            host_ip = socket.gethostbyname(host)
            status = False

            # create instance of socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # connecting the host ip address and port
            s.connect((host_ip, port))
            try:
                banner = s.recv(1024).decode()
                print("Port {} is open with banner {}".format(port, banner))

            except:
                print("Port {} is open ".format(port))

        except:
            pass  # Silently ignore closed ports (optional)

    # Example port range to scan (e.g., 1 to 100)
    port_range_start = 1
    port_range_end = 100

    threads = []
    for port in range(port_range_start, port_range_end + 1):
        t = threading.Thread(target=scanner, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Wait for all threads to complete
    ```

## Configuration Options

*   **Host:**  Edit the `host` variable in `BannerGrabber.py` to specify the target host IP address or hostname.
*   **Port Range:**  The script currently scans one port at a time.  Modify the script to iterate through a range of ports for a wider scan.

## Contributing Guidelines

Contributions are welcome! Here's how you can contribute:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Test your changes thoroughly.
5.  Submit a pull request with a clear description of your changes.

