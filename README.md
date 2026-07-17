# EcoTouch ERP

<div align="center">
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-5.8-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Vite-7-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/Tauri-2-24C8DB?style=for-the-badge&logo=tauri&logoColor=white" alt="Tauri" />
  <img src="https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" />
</div>

<p align="center">
  <strong>A modern ERP experience for operations, inventory, production, and decision-making.</strong>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/line-break.png" alt="divider" />
</p>

EcoTouch ERP is a polished, high-performance business management platform designed for teams that need speed, structure, and clarity across procurement, production, inventory, attendance, and approvals. Its interface blends modern UI design with practical workflow automation to support both daily operations and strategic insight.

## ✨ Highlights

- Sleek, responsive dashboard experience
- Unified workflows for inward, outward, and production processes
- Smart inventory and material management
- Role-based navigation and approval systems
- Reporting and analytics designed for operational visibility
- Desktop-ready deployment with Tauri for a native feel

## 🧩 Core Modules

- Dashboard & analytics
- Inward and outward operations
- Production planning and BOM management
- Inventory, materials, and products
- Workers, users, roles, and approvals
- Logistics, vehicles, and reporting

## 🛠️ Tech Stack

- React 19 + TypeScript
- Vite for lightning-fast development
- Tailwind CSS for modern UI styling
- TanStack Query for state and data flow
- Recharts for interactive charts and insights
- Supabase for authentication and storage
- Tauri for desktop application packaging

## 📁 Project Structure

- src/pages — application screens and business views
- src/components — reusable UI and feature components
- src/hooks — custom hooks for realtime and resource handling
- src/lib — shared utilities, formatting, and API helpers
- src-tauri — desktop integration and packaging configuration

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

- Node.js 20+
- npm or pnpm
- Rust and Tauri prerequisites for desktop builds

### Installation

```bash
git clone https://github.com/your-username/ecotouch-erp.git
cd ecotouch-erp
npm install
```

### Environment Setup

Create a .env file in the project root:

```env
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
```

### Run Locally

```bash
npm run dev
```

### Run Desktop App

```bash
npm run tauri dev
```

### Build for Production

```bash
npm run build
```

> The application is designed to run both as a web app and as a desktop experience, giving teams flexibility without sacrificing consistency.

## 🌐 Why It Matters

EcoTouch ERP is built to reduce friction between operations and management, helping teams make faster decisions with better visibility and less manual overhead.

## 🤝 Contributing

Contributions are welcome. Please fork the repository, create a feature branch, and open a pull request with your changes.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 📬 Contact

For questions, feedback, or collaboration, please open an issue or start a discussion in the repository.
