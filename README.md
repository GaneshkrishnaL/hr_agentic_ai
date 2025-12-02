# HR Agentic AI

HR Agentic AI is a comprehensive Human Resource Management System (HRMS) built as a **Model Context Protocol (MCP)** server. It provides an AI-powered interface for managing employees, leaves, meetings, and support tickets, designed to be integrated with LLM-based agents.

## 🚀 Features

### 👥 Employee Management
- **Onboarding**: Streamlined process to add new employees.
- **Directory**: Search and retrieve employee details.
- **Hierarchy**: Manage reporting lines (managers and direct reports).

### 📅 Leave Management
- **Tracking**: Maintain leave balances and history.
- **Applications**: Apply for leaves with automatic balance validation.
- **History**: View past leave records.

### 🗓️ Meeting Management
- **Scheduling**: Book meetings with conflict detection.
- **Calendar**: View scheduled meetings for any employee.
- **Cancellations**: Cancel existing meetings.

### 🎫 Ticket Management
- **Requests**: Create tickets for IT assets (laptops, IDs, etc.).
- **Workflow**: Track and update ticket status (Open, In Progress, Closed).
- **History**: List tickets by employee or status.

### 📧 Communication
- **Email Integration**: Automated email notifications for onboarding and updates.

## 🛠️ Technology Stack

- **Python 3.10+**
- **MCP (Model Context Protocol)**: For agentic tool exposure.
- **FastMCP**: High-performance MCP server implementation.
- **Pydantic**: Data validation and schema definition.
- **UV**: Fast Python package installer and resolver.

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GaneshkrishnaL/hr_agentic_ai.git
   cd hr_agentic_ai
   ```

2. **Set up Virtual Environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate it
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**
   We use `uv` for fast installation, but standard pip works too.
   ```bash
   pip install uv
   uv pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```

2. Add your configuration details (required for email functionality):
   ```env
   email=your_email@gmail.com
   pwd=your_app_password
   ```
   > **Note**: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833), not your regular login password.

## 🏃‍♂️ Usage

### Running the MCP Server   

## MCP Server - Client Configuration  https://modelcontextprotocol.io/docs/develop/build-server

You can run the server directly using Python:

```bash
python server.py
```

Or configure it in your MCP client (like Claude Desktop):

```json
{
  "mcpServers": {
    "hr_agentic_ai": {
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/hr_agentic_ai",
        "run",
        "server.py"
      ],
      "env": {
        "email": "your_email@gmail.com",
        "pwd": "your_app_password"
      }
    }
  }
}
```

### Available Tools

The server exposes the following tools to the AI agent:

- `add_employee(emp_name, manager_id, emp_email)`
- `get_employee(name)`
- `apply_leave(emp_id, leave_dates)`
- `get_employee_leave_balance(emp_id)`
- `schedule_meeting(employee_id, meeting_datetime, topic)`
- `create_ticket(emp_id, item, reason)`
- `send_email(subject, body, to_emails)`
- ...and more.

### Example Workflow (Prompt)

You can ask the agent to perform complex tasks like:

> "Onboard a new employee named Alice. Her manager is Sarah (E001). Send her a welcome email and request a laptop for her."

The agent will use the `onboard_new_employee` prompt or chain multiple tools to complete this request.

## 📂 Project Structure

```
hr_agentic_ai/
├── HRMS/                  # Core Business Logic
│   ├── __init__.py
│   ├── employee_manager.py
│   ├── leave_manager.py
│   ├── meeting_manager.py
│   ├── ticket_manager.py
│   └── schemas.py         # Pydantic Models
├── server.py              # MCP Server Entry Point
├── utils.py               # Data Seeding & Utilities
├── emails.py              # Email Service
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
