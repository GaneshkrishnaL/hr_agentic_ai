from utils import seed_services
from HRMS import *
from typing import List,Dict,Optional

from mcp.server.fastmcp import FastMCP
import os 


employee_manager = EmployeeManager()
leave_manager = LeaveManager()
meeting_manager = MeetingManager()
ticket_manager = TicketManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)

mcp=FastMCP("HR Agentic AI")

@mcp.tool()
def add_employee(emp_name:str,manager_id:str,emp_email:str)->str:
    """
    Adds a new employee to the system.
    
    Args:
        emp_name (str): Name of the employee
        manager_id (str): ID of the employee's manager
        emp_email (str): Email address of the employee
    
    Returns:
        str: Confirmation message
    """
    emp=EmployeeCreate(emp_id=employee_manager.get_next_emp_id(),name=emp_name,manager_id=manager_id,email=emp_email)
    employee_manager.add_employee(emp)
    return f"Employee {emp_name} added successfully"

@mcp.tool()
def get_employee(name:str)->Dict[str,str]:
    """
    Retrieves an employee's details.
    
    Args:
        name (str): Name of the employee
    
    Returns:
        Dict[str,str]: Employee details
    """
    eid=employee_manager.search_employee_by_name(name)
    if len(eid)==0:
        return "Employee not found"
    emp_id=eid[0]
    return employee_manager.get_employee_details(emp_id)










if __name__ == "__main__":
    mcp.run(transport="stdio")
    