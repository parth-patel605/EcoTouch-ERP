# EcoTouch ERP

<div align="center">
  <img src="https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-5.8-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Vite-7-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/Tauri-2-24C8DB?style=for-the-badge&logo=tauri&logoColor=white" alt="Tauri" />
  <img src="https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase" />
</div>

EcoTouch ERP is a refined, high-performance business management platform crafted for modern organizations that need clarity, control, and speed across operations. From procurement to production, inventory to approvals, the system delivers a unified experience designed for daily execution and strategic oversight.

## Executive Overview

EcoTouch ERP combines elegant interface design with practical workflow automation to help teams manage:

- Procurement and inward operations
- Production planning and BOM workflows
- Inventory and raw material control
- Sales, dispatch, and outward processes
- Attendance, worker coordination, and approvals
- Reporting and analytics with business intelligence in mind

## Premium Features

- Modern, responsive dashboard experience
- Role-based navigation and access structure
- Streamlined management for products, materials, and inventory
- Operational modules for production, logistics, and vehicles
- Approval workflows and user administration
- Desktop-ready deployment with Tauri for a native experience

## Technology Stack

- React 19 with TypeScript
- Vite for fast local development and optimized builds
- Tailwind CSS for polished, scalable UI design
- TanStack Query for efficient async state handling
- Recharts for rich dashboards and data visualization
- Supabase for authentication and database integration
- Tauri for desktop application packaging

## Project Architecture

- src/pages — core application views and business modules
- src/components — reusable interface and feature components
- src/hooks — custom hooks for realtime and resource handling
- src/lib — shared utilities, API integration, and formatting helpers
- src-tauri — native desktop configuration and packaging

## Getting Started

### Prerequisites

Ensure the following are installed on your machine:

- Node.js 20 or newer
- npm or pnpm
- Rust and the required Tauri dependencies for desktop builds

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/ecotouch-erp.git
   cd ecotouch-erp
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Configure environment variables

   Create a .env file in the project root with your Supabase credentials:
   ```env
   VITE_SUPABASE_URL=your_supabase_project_url
   VITE_SUPABASE_ANON_KEY=your_supabase_anon_key
   ```

### Run the web application

```bash
npm run dev
```

Open the local app at http://localhost:1420.

### Run the desktop application

```bash
npm run tauri dev
```

### Build for production

```bash
npm run build
```

## Development Philosophy

The product is designed to balance simplicity and sophistication, giving teams a dependable system that feels modern, intuitive, and enterprise-ready.

## Contributing

Contributions are welcome. If you would like to help improve the platform, please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License

This project is distributed under the MIT License. See the LICENSE file for more details.

## Contact

For inquiries, feedback, or collaboration, please open an issue or start a discussion in the repository.
