#!/usr/bin/env python3
import asyncio
import argparse

async def grab_banner(host: str, port: int, timeout: int = 5) -> str:
    """Connect asynchronously to host:port and attempt to retrieve a banner."""
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )

        # Protocol-specific probes
        if port == 80:  # HTTP
            writer.write(b"HEAD / HTTP/1.0\r\n\r\n")
        elif port == 21:  # FTP
            writer.write(b"\r\n")
        elif port == 25:  # SMTP
            writer.write(b"EHLO example.com\r\n")
        elif port == 22:  # SSH
            # SSH servers usually send a banner immediately, no probe needed
            pass
        elif port == 3389:  # RDP
            # RDP requires a specific handshake, but we can send a dummy packet
            writer.write(b"\x03\x00\x00\x13\x0e\xd0\x00\x00\x12\x34\x00\x02\x00\x08\x00\x03\x00\x00\x00")
        else:
            writer.write(b"\r\n")

        await writer.drain()

        banner = await asyncio.wait_for(reader.read(1024), timeout=timeout)
        writer.close()
        await writer.wait_closed()

        return banner.decode(errors="ignore").strip() or "No banner received."
    except asyncio.TimeoutError:
        return "Connection timed out."
    except ConnectionRefusedError:
        return "Connection refused."
    except Exception as e:
        return f"Error: {e}"

async def scan_targets(targets, timeout=5):
    tasks = [grab_banner(host, port, timeout) for host, port in targets]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return {
        (host, port): (res if isinstance(res, str) else f"Error: {res}")
        for (host, port), res in zip(targets, results)
    }

def main():
    parser = argparse.ArgumentParser(description="Async Banner Grabber with SSH/RDP support")
    parser.add_argument("targets", nargs="+", help="Targets in host:port format (e.g. 192.168.1.10:22)")
    parser.add_argument("--timeout", type=int, default=5, help="Connection timeout in seconds")
    parser.add_argument("--output", help="Optional file to save results")
    args = parser.parse_args()

    target_list = []
    for t in args.targets:
        try:
            host, port = t.split(":")
            target_list.append((host, int(port)))
        except ValueError:
            print(f"[!] Invalid target format: {t} (use host:port)")

    print(f"[+] Scanning {len(target_list)} targets asynchronously...")
    results = asyncio.run(scan_targets(target_list, timeout=args.timeout))

    for (host, port), banner in results.items():
        print(f"\n--- {host}:{port} ---\n{banner}")

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            for (host, port), banner in results.items():
                f.write(f"{host}:{port}\n{banner}\n\n")
        print(f"[+] Results saved to {args.output}")

if __name__ == "__main__":
    main()
