# Website Blocker & Unblocker

This is a simple Python application that allows you to block or unblock websites by modifying the system's `hosts` file. The application is built using the Tkinter library for the graphical user interface (GUI).

## Features

- **Block Websites:** Add a website to the system's `hosts` file to block access to it.
- **Unblock Websites:** Remove a website from the system's `hosts` file to unblock access.
- **User-Friendly GUI:** The application features an intuitive graphical interface for easy interaction.

## How It Works

The application works by adding or removing entries in the system's `hosts` file. The `hosts` file maps domain names to IP addresses. By mapping a domain name to `127.0.0.1` (the local machine), the application effectively blocks access to that website on the system.

### File Location

- **Windows:** `C:\Windows\System32\drivers\etc\hosts`
- **Linux/macOS:** `/etc/hosts` (Note: This path is not used in the current version, which is Windows-specific).

## Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system.
- **Tkinter:** Tkinter is included with most Python installations. If it’s not available, you can install it using:
  ```bash
  pip install tk
