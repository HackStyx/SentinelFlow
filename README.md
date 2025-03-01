# SentinelFlow 🛡

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Electron Version](https://img.shields.io/badge/electron-latest-blue.svg)](https://www.electronjs.org/)
[![GitHub Issues](https://img.shields.io/github/issues/HackStyx/SentinelFlow)](https://github.com/HackStyx/SentinelFlow/issues)
[![GitHub Stars](https://img.shields.io/github/stars/HackStyx/SentinelFlow)](https://github.com/HackStyx/SentinelFlow/stargazers)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Scapy](https://img.shields.io/badge/Scapy-FF0000?style=flat&logo=python&logoColor=white)](https://scapy.net/)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-AI-green)](https://langchain.com/)

<h3>Next-Generation Network Security with AI-Powered Threat Detection</h3>

</div>

## 🌟 Overview

SentinelFlow is an advanced network security monitoring and threat detection system that combines real-time packet analysis with AI-powered threat detection. Built with a modern tech stack including Python, Electron, and React, it provides a seamless and intuitive interface for monitoring network traffic and identifying potential security threats.

<div align="center">
<img src="https://github.com/user-attachments/assets/a154d945-4359-40ea-80ff-158239b8e183" alt="SentinelFlow Architecture" width="800"/>
</div>

## 🎯 Why SentinelFlow?

- *Intelligent Threat Detection*: Leverages multiple AI agents for comprehensive security analysis
- *Real-time Monitoring*: Zero-latency packet analysis and instant threat alerts
- *User-Friendly Interface*: Modern, intuitive UI for both beginners and security experts
- *Extensible Architecture*: Easy to add new threat detection capabilities
- *Cross-Platform*: Works seamlessly on Windows, macOS, and Linux

## ✨ Key Features

### 🔍 Network Analysis
- *Real-time Packet Capture*: Powered by Scapy for high-performance packet interception
- *Protocol Support*: TCP, UDP, HTTP/S, DNS, and more
- *Traffic Visualization*: Real-time network traffic patterns and anomaly detection
- *Packet Filtering*: Custom filters for targeted monitoring

### 🤖 AI-Powered Security
- *Multi-Agent System*:
  - XSS Detection Agent
  - SQL Injection Analysis Agent
  - Payload Analysis Agent
  - Decision Making System
- *Machine Learning Models*: Pattern recognition for zero-day threats
- *Natural Language Processing*: Query your network logs in plain English

### 🛠 Security Profiles
- *Pre-configured Templates*:
  - Backend Infrastructure Protection
  - Web Application Security
  - Database Access Monitoring
  - General Network Usage
- *Custom Profile Creation*: Build your own security rules

### 📊 Analytics & Reporting
- *Real-time Dashboard*: Live network statistics and threat alerts
- *Detailed Logs*: Comprehensive activity tracking
- *Export Capabilities*: Generate detailed security reports
- *Visualization*: Interactive charts and graphs

## 🚀 Getting Started

### System Requirements

- *OS*: Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- *CPU*: 2+ cores recommended
- *RAM*: 4GB minimum, 8GB recommended
- *Storage*: 1GB free space
- *Network*: Active internet connection

### Prerequisites

- Python 3.11 or higher
- Node.js 16+ and npm
- Administrative privileges (for packet capture)

### Quick Start

1. **Clone & Setup**:
   ```bash
   # Clone repository
   git clone https://github.com/HackStyx/SentinelFlow.git
   cd SentinelFlow

   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   cd frontend && npm install
   

2. **Configure Environment**:
   ```bash
   # Copy example environment file
   cp .env.example .env
   # Edit .env with your settings
   nano .env  # or use VS Code: "code .env", Notepad: "notepad .env", etc.

   

3. **Launch Application**:
   ```bash
   # Terminal 1: Start backend
   cd backend
   python server.py

   # Terminal 2: Start frontend
   cd frontend
   npm run dev
   

## 🏗 Architecture

SentinelFlow follows a microservices architecture with these key components:

- *Frontend*: Electron + React application for UI
- *Backend*: FastAPI server for API endpoints
- *AI Engine*: LangChain-based multi-agent system
- *Packet Capture*: Scapy-powered network monitoring
- *Database*: Vector store for semantic log searching


## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



---

