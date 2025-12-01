# Banner-Grabber

A basic Python banner grabbing script to find Open Ports of any hosts and grab banners of services available on different ports.

## Key Features & Benefits

*   **Port Scanning:** Identifies open ports on a specified host.
*   **Banner Grabbing:** Retrieves service banners from open ports, revealing information about running services.
*   **Threaded Scanning:** Implements asynchronous scanning for faster port scanning.

## Prerequisites & Dependencies

*   **Python 3.7+:**  This script requires Python 3.7 or higher due to the usage of `asyncio`.
*   **asyncio:**  Python's built-in asynchronous I/O library (no external installation required).

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Paddywelch117/Banner-Grabber.git
    cd Banner-Grabber
    ```

2.  **Verify Python Installation:**

    ```bash
    python3 --version
    ```
    Ensure that the version is 3.7 or higher.

3.  **No additional packages required!**  The script uses only built-in Python libraries.

## Usage Examples

**Running the Script:**

```bash
python3 banner_grabber.py <target_host> -p <port1,port2,port3> -t <timeout>
```

**Example:**

```bash
python3 banner_grabber.py example.com -p 21,22,80,443 -t 3
```

This will scan ports 21, 22, 80, and 443 on `example.com` with a timeout of 3 seconds.

## Configuration Options

*   **Target Host:** Specify the target host as the first argument to the script.
*   **Ports (-p or --ports):**  A comma-separated list of ports to scan. Defaults to "21,22,80,443".
*   **Timeout (-t or --timeout):**  The timeout in seconds for each connection.  Defaults to 5 seconds.

## Contributing Guidelines

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License Information

No license specified. All rights reserved.

## Acknowledgments

*   The `asyncio` library for providing asynchronous capabilities in Python.
