# Django Todo App - Full-Featured Task Management System

A comprehensive Django-based todo application with advanced task management features including status tracking, priority levels, date-based organization, search functionality, and full CRUD operations. Built using Test-Driven Development (TDD) methodology as part of EECE 4081 Software Engineering coursework.

**Student**: Sara Howell  
**Course**: EECE 4081 - Fall 2025  
**Repository**: https://github.com/eece-4081-fall-2025/sara_howell_todo

---

## Table of Contents

- [Features](#features)
- [Development Methodology](#development-methodology)
- [Development Stack](#development-stack)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage Guide](#usage-guide)
- [Architecture and Design](#architecture-and-design)
- [Testing](#testing)
- [TDD Evidence](#tdd-evidence)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Future Enhancements](#future-enhancements)

---

## Features

### Core Task Management (Sprint 1 - Completed)

1. **Task Creation**
   - Quick add functionality for rapid task entry
   - Detailed form for comprehensive task creation
   - Optional due date assignment
   - Priority level selection (High, Medium, Low)
   - Automatic timestamp tracking (created_at, updated_at)

2. **Status Management**
   - Three-state status system: Pending, Done, Skipped
   - Visual indicators for each status with color coding
   - One-click status updates
   - Undo functionality to revert status changes
   - Status transitions fully tested

3. **Priority System** (TDD Cycle 1)
   - Three priority levels: High, Medium, Low
   - Default priority: Medium
   - Visual priority badges with distinct colors:
     - High: Red background
     - Medium: Yellow background
     - Low: Gray background
   - Priority field included in both quick add and detailed forms

4. **Search Functionality** (TDD Cycle 2)
   - Case-insensitive search across task names
   - Partial match support
   - Search box integrated into main page
   - Dedicated search results page
   - Result count display
   - Empty search returns all tasks

5. **Task Editing**
   - Full edit capabilities for all task attributes
   - Edit tasks from any time period (past, present, future)
   - Confirmation dialogs for destructive actions
   - Real-time validation
   - Status and priority updates

6. **Task Deletion**
   - Confirmation-based deletion to prevent accidents
   - Warning page with task details
   - Permanent removal with user acknowledgment

7. **Smart Organization**
   - Automatic categorization by date:
     - 🚨 Overdue Tasks (past due, still pending)
     - 📅 Today's Tasks (due today)
     - 🔮 Upcoming Tasks (future due dates)
     - 📋 Tasks Without Due Dates
   - Color-coded visual organization
   - Automatic sorting by due date and creation time

8. **Overdue Detection**
   - Computed `is_overdue` property on model
   - Only marks pending tasks as overdue
   - Completed/skipped tasks ignore due dates
   - Visual warning indicators

---

## Development Methodology

### Test-Driven Development (TDD)

This project was developed using strict TDD methodology with clear Red-Green-Refactor cycles:

**TDD Cycle 1: Task Priority System**
- **RED**: Wrote 5 failing tests for priority feature
- **GREEN**: Implemented priority field with choices (low, medium, high)
- **REFACTOR**: Added visual priority badges and improved UX

**TDD Cycle 2: Task Search Functionality**
- **RED**: Wrote 7 failing tests for search feature
- **GREEN**: Implemented search view with case-insensitive filtering
- **REFACTOR**: Integrated search box into main page

All TDD cycles are documented in Git commit history with clear commit messages showing each phase.

### Test Coverage

- **40+ comprehensive tests** covering all functionality
- Model tests (15+ tests)
- Form tests (5+ tests)
- View tests (15+ tests)
- Integration tests (5+ tests)
- 100% coverage of critical business logic

---

## Development Stack

### Core Technologies
- **Programming Language**: Python 3.12.6
- **Web Framework**: Django 5.2.6
- **Database**: SQLite3 (development)
- **Version Control**: Git
- **Repository Hosting**: GitHub

### Development Tools
- **IDE**: Visual Studio Code
- **Virtual Environment**: venv (Python standard library)
- **Template Engine**: Django Templates
- **Form Handling**: Django Forms with ModelForms
- **Testing**: Django TestCase framework

### Key Django Components Used
- Models with choices and computed properties
- Function-based views with full CRUD operations
- Django Messages framework for user feedback
- Django Forms with custom widgets
- URL routing with named patterns
- Template inheritance and custom styling
- Django ORM for database queries

---

## Project Structure

```
sara_howell_todo/
├── five/                          # Django project directory
│   ├── __init__.py
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Root URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
│
├── todo/                          # Main application
│   ├── migrations/               # Database migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_add_priority.py
│   │
│   ├── templates/                # HTML templates
│   │   └── todo/
│   │       ├── todo_list.html           # Main task list view
│   │       ├── todo_form.html           # Create/Edit form
│   │       ├── todo_confirm_delete.html # Delete confirmation
│   │       └── todo_search.html         # Search results page
│   │
│   ├── __init__.py
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Data models (ToDo)
│   ├── views.py                  # View functions (8 views)
│   ├── urls.py                   # App URL patterns
│   ├── forms.py                  # Form definitions (2 forms)
│   └── tests.py                  # Comprehensive test suite (40+ tests)
│
├── manage.py                      # Django management script
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
└── db.sqlite3                    # SQLite database file
```

---

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/eece-4081-fall-2025/sara_howell_todo.git
cd sara_howell_todo
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- Django==5.2.6
- (All other standard library dependencies)

### Step 4: Run Database Migrations

```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account for accessing `/admin/`.

### Step 6: Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser.

### Step 7: Run Tests (Verify Installation)

```bash
python manage.py test
```

Should show: `Ran 40+ tests ... OK`

---

## Usage Guide

### Creating Tasks

**Quick Add (Homepage):**
1. Enter task description in the "What needs to be done?" field
2. Optionally select a due date
3. Select priority (High, Medium, or Low)
4. Click "Add Task"
5. Task is created with default "Pending" status

**Detailed Creation:**
1. Click "Create Task" or navigate to `/create/`
2. Fill in task details:
   - Task name (required)
   - Due date (optional)
   - Priority (Low/Medium/High)
   - Status (Pending/Done/Skipped)
3. Click "Create Task"

### Searching for Tasks

**From Main Page:**
1. Use the search box at the top of the page
2. Enter search term (searches task names)
3. Click "Search" button
4. View results on dedicated search page

**Direct Search:**
- Navigate to `/search/?q=your_search_term`
- Search is case-insensitive
- Supports partial matches

### Managing Task Status

**Mark as Done:**
- Click the green "✓ Done" button on any pending task
- Task moves to completed state with visual strikethrough
- Status badge turns green

**Mark as Skipped:**
- Click the gray "⊘ Skip" button on any pending task
- Task is marked skipped and visually de-emphasized
- Status badge turns gray

**Undo Status:**
- Click the yellow "↺ Undo" button on completed/skipped tasks
- Task returns to pending status
- Can re-mark as done/skipped

### Understanding Priority Levels

**High Priority (Red Badge):**
- Urgent tasks requiring immediate attention
- Displayed with red priority indicator
- Use for critical deadlines

**Medium Priority (Yellow Badge):**
- Default priority level
- Standard importance tasks
- Most common priority level

**Low Priority (Gray Badge):**
- Non-urgent tasks
- Can be completed when time permits
- Flexible scheduling

### Editing Tasks

1. Click the "✎ Edit" button on any task
2. Modify any field:
   - Task name
   - Due date
   - Priority level
   - Status
3. Click "Edit Task" to save changes
4. Or click "Cancel" to discard changes

**Note**: You can edit tasks from any time period - past, present, or future.

### Deleting Tasks

1. Click the red "✗ Delete" button on any task
2. Review the confirmation page showing:
   - Task name
   - Warning message
3. Click "Yes, Delete It" to permanently remove
4. Or click "Cancel" to return without deleting

### Viewing Organized Tasks

Tasks are automatically organized into sections on the main page:

- **Overdue Tasks**: Past due date, still pending (red indicator)
- **Today's Tasks**: Due today (green indicator)
- **Upcoming Tasks**: Future due dates (blue indicator)
- **No Due Date**: Tasks without assigned dates

Each section shows:
- Task name
- Status badge (Pending/Done/Skipped)
- Priority badge (High/Medium/Low)
- Due date (if applicable)
- Action buttons

---

## Architecture and Design

### Model Design

**ToDo Model** (`todo/models.py`)

```python
class ToDo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('skipped', 'Skipped'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Key Design Decisions:**
- Used `CharField` with choices for status and priority (extensible, database-efficient)
- Separated creation and update timestamps for audit trail
- Made due_date optional for flexibility
- Added `is_overdue` computed property for business logic
- Implemented custom ordering by due date, then creation time
- Default values ensure data consistency

### View Architecture

**Function-Based Views** for simplicity and clarity:

| View Function | Purpose | HTTP Methods |
|--------------|---------|--------------|
| `todo_list` | Main view with date organization + quick add | GET, POST |
| `todo_create` | Detailed task creation form | GET, POST |
| `todo_edit` | Task modification | GET, POST |
| `todo_delete` | Confirmation-based deletion | GET, POST |
| `todo_mark_done` | Set status to done | GET |
| `todo_mark_skipped` | Set status to skipped | GET |
| `todo_mark_pending` | Revert to pending | GET |
| `todo_search` | Search tasks by name | GET |

**Design Pattern**: Each view follows Django best practices:
- GET requests display forms/data
- POST requests process form submissions
- Redirects after successful POST (PRG pattern)
- User feedback via Django Messages framework
- Proper error handling

### Form Design

**Two-Form Strategy:**

1. **QuickAddForm**: Minimal fields for rapid task entry
   - Name (required)
   - Due date (optional)
   - Priority (optional, defaults to medium)
   - Auto-sets status to "pending"

2. **TodoForm**: Complete task management
   - Name (required)
   - Due date (optional)
   - Priority (required, with all choices)
   - Status (required, with all choices)

**Benefits**: 
- Optimized UX for different use cases
- No form duplication
- Consistent validation
- Custom widgets for better UX

### Template Design

**Design Principles:**
- Self-contained templates with inline CSS
- Consistent color scheme throughout
- Responsive design with modern gradients
- Visual hierarchy with proper spacing
- Accessibility considerations

**Color Scheme:**
- Purple/blue gradients for headers
- Yellow for pending tasks
- Green for completed tasks
- Gray for skipped tasks
- Red for overdue warnings and high priority

**Priority Colors:**
- High: Red (#dc3545)
- Medium: Yellow (#ffc107)
- Low: Gray (#6c757d)

---

## Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test class
python manage.py test todo.tests.ToDoModelTests
python manage.py test todo.tests.TaskPriorityTests
python manage.py test todo.tests.TaskSearchTests

# Run with verbose output
python manage.py test --verbosity=2

# Run specific test method
python manage.py test todo.tests.ToDoModelTests.test_is_overdue_property_with_past_date
```

### Test Coverage Breakdown

**Model Tests (ToDoModelTests)**: 15+ tests
- Basic CRUD operations
- String representation
- Default values
- Status choices validation
- Priority choices validation
- Due date handling
- `is_overdue` property (all edge cases)
- Timestamp functionality
- Custom ordering

**Priority Tests (TaskPriorityTests)**: 5+ tests
- Priority field existence
- Default priority value
- All priority choices
- Priority display in views
- Priority ordering

**Form Tests (TodoFormTests, QuickAddFormTests)**: 5+ tests
- Valid data submission
- Required field validation
- Optional field handling
- Invalid status handling
- Priority field validation

**View Tests (TodoViewTests)**: 15+ tests
- All CRUD endpoints
- GET and POST requests
- Status transitions
- Date-based organization
- Redirect behavior
- 404 handling
- Template usage
- Message framework integration

**Search Tests (TaskSearchTests)**: 7+ tests
- Search endpoint existence
- Matching results return
- Case-insensitive search
- Empty query handling
- No results handling
- Partial match support
- Result count display

**Integration Tests (TodoIntegrationTests)**: 5+ tests
- Complete task lifecycle
- Date filtering accuracy
- Multiple tasks handling
- Real-world workflows
- Status transition sequences

**Total Test Count**: 40+ comprehensive tests

### Test Data

Tests use Django's TestCase with automatic database setup/teardown:
- Isolated test database
- Fresh data for each test
- No pollution between tests
- Automatic cleanup

---

## TDD Evidence

### Commit History Shows TDD Methodology

The Git commit history provides clear evidence of Test-Driven Development:

#### TDD Cycle 1: Task Priority System

1. **RED Phase** - Commit: "TDD Cycle 1 RED: Add failing tests for task priority feature"
   - Added 5 tests for priority functionality
   - Tests failed (feature didn't exist yet)
   - Demonstrated test-first approach

2. **GREEN Phase** - Commit: "TDD Cycle 1 GREEN: Implement task priority feature - tests now passing"
   - Added PRIORITY_CHOICES to model
   - Added priority field with default='medium'
   - Created migrations
   - Updated forms to include priority
   - All tests passed

3. **REFACTOR Phase** - Commit: "TDD Cycle 1 REFACTOR: Add visual priority indicators and improve UX"
   - Added priority badges to templates
   - Improved visual design
   - Enhanced user experience
   - Tests still passed

#### TDD Cycle 2: Task Search Functionality

4. **RED Phase** - Commit: "TDD Cycle 2 RED: Add failing tests for task search functionality"
   - Added 7 tests for search feature
   - Tests failed (search view didn't exist)
   - Tested various search scenarios

5. **GREEN Phase** - Commit: "TDD Cycle 2 GREEN: Implement task search feature - tests now passing"
   - Created todo_search view
   - Added search URL pattern
   - Created search template
   - Implemented case-insensitive filtering
   - All tests passed

6. **REFACTOR Phase** - Commit: "TDD Cycle 2 REFACTOR: Add search box to main page for better UX"
   - Integrated search box into main page
   - Improved navigation
   - Enhanced user workflow
   - Tests still passed

### Viewing TDD Evidence

To view the TDD commit history:

```bash
git log --oneline --grep="TDD"
```

Or view on GitHub:
```
https://github.com/eece-4081-fall-2025/sara_howell_todo/commits/main
```

---

## API Endpoints

| URL Pattern | View Function | HTTP Methods | Purpose |
|------------|---------------|--------------|---------|
| `/` | `todo_list` | GET, POST | Main list view + quick add |
| `/create/` | `todo_create` | GET, POST | Detailed task creation |
| `/edit/<id>/` | `todo_edit` | GET, POST | Edit existing task |
| `/delete/<id>/` | `todo_delete` | GET, POST | Delete confirmation |
| `/mark-done/<id>/` | `todo_mark_done` | GET | Mark task as done |
| `/mark-skipped/<id>/` | `todo_mark_skipped` | GET | Mark task as skipped |
| `/mark-pending/<id>/` | `todo_mark_pending` | GET | Revert to pending |
| `/search/` | `todo_search` | GET | Search tasks by name |
| `/admin/` | Django Admin | ALL | Admin interface |

**RESTful Principles:**
- Clear, semantic URL patterns
- Appropriate HTTP methods
- Resource-based naming
- Predictable endpoints
- Query parameters for search

**Example API Calls:**
```
GET /                           # View all tasks
POST / (form data)             # Quick add task
GET /search/?q=buy             # Search for "buy"
GET /mark-done/5/              # Mark task 5 as done
POST /edit/3/ (form data)      # Update task 3
```

---

## Database Schema

### ToDo Table

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key, Auto-increment | Unique identifier |
| name | CharField(255) | NOT NULL | Task description |
| status | CharField(10) | NOT NULL, Choices | Current status (pending/done/skipped) |
| priority | CharField(10) | NOT NULL, Choices, Default='medium' | Priority level (low/medium/high) |
| due_date | DateField | NULL, BLANK | Optional deadline |
| created_at | DateTimeField | NOT NULL, Auto-add | Creation timestamp |
| updated_at | DateTimeField | NOT NULL, Auto-update | Last modification timestamp |

**Indexes:**
- Primary key on `id`
- Ordering index on `(due_date, -created_at)`

**Constraints:**
- `status` must be in ['pending', 'done', 'skipped']
- `priority` must be in ['low', 'medium', 'high']
- `name` max length 255 characters
- `status` default: 'pending'
- `priority` default: 'medium'

**Relationships:**
- Currently no foreign keys (single-user system)
- Future: Add User foreign key for multi-user support

---

## Future Enhancements

### Planned Features (Sprint 2+)

1. **User Authentication**
   - Multi-user support
   - Personal task lists
   - User registration/login
   - Permission system

2. **Task Categories/Tags**
   - Categorization system
   - Multiple tags per task
   - Tag-based filtering
   - Color-coded categories

3. **Recurring Tasks**
   - Daily/Weekly/Monthly recurrence
   - Auto-creation of recurring instances
   - Recurrence pattern management
   - Skip recurring instances

4. **Advanced Search**
   - Search by priority
   - Search by status
   - Search by date range
   - Combined filters
   - Saved searches

5. **Notifications**
   - Due date reminders
   - Overdue notifications
   - Email integration
   - Browser notifications

6. **Task Notes/Comments**
   - Detailed task descriptions
   - Comment system
   - Markdown support
   - File attachments

7. **Statistics Dashboard**
   - Completion rates
   - Productivity analytics
   - Visual charts and graphs
   - Time tracking

8. **Export/Import**
   - CSV export
   - JSON export
   - Import from other apps
   - Backup functionality

9. **Subtasks**
   - Break tasks into subtasks
   - Progress tracking
   - Hierarchical structure
   - Checklist functionality

10. **Mobile Optimization**
    - Responsive design improvements
    - Touch-friendly interface
    - Progressive Web App (PWA)
    - Mobile-specific features

---

## Development Notes

### Sprint 1 Completion Status

✅ All Core Task Creation epic user stories completed:
1. ✅ Create tasks with text
2. ✅ Mark tasks as done or skipped
3. ✅ Edit tasks after creation
4. ✅ Delete tasks
5. ✅ Edit previous days' tasks
6. ✅ Edit future days' tasks

✅ Additional features implemented via TDD:
7. ✅ Task priority system (High/Medium/Low)
8. ✅ Task search functionality

### Code Quality

- Clean, maintainable code following PEP 8 style guide
- Comprehensive docstrings for all functions
- Proper error handling with user feedback
- Separation of concerns (models, views, forms, templates)
- DRY principles applied throughout
- No code duplication
- Meaningful variable and function names

### Performance Considerations

- Efficient database queries
- Proper use of Django ORM
- Minimal template logic
- No N+1 query problems
- Future: Query optimization with select_related/prefetch_related
- Future: Caching for frequently accessed data

### Security Considerations

- CSRF protection on all forms
- SQL injection prevention via Django ORM
- XSS protection via Django template escaping
- Future: Rate limiting for search
- Future: User authentication and authorization

---

## Contributing

This is a student project for EECE 4081. For questions or suggestions, please contact:

**Sara Howell**  
Email: sfhowell@memphis.edu  
GitHub: [@sfhowell](https://github.com/sfhowell)

---

## License

This project is created for educational purposes as part of EECE 4081 coursework at the University of Memphis.

---

## Acknowledgments

- **Professor**: EECE 4081 Fall 2025 Instructor
- **Framework**: Django Software Foundation
- **Inspiration**: Modern task management applications (Todoist, Microsoft To Do)
- **Design**: Contemporary web design principles
- **Methodology**: Test-Driven Development best practices

---

## Version History

### Version 1.1 (Current) - September 2025
- Added task priority system (TDD Cycle 1)
- Added task search functionality (TDD Cycle 2)
- Comprehensive test suite (40+ tests)
- Full TDD documentation
- Enhanced user interface

### Version 1.0 (Sprint 1) - September 2025
- Initial release
- Core CRUD operations
- Status management system
- Date-based organization
- Basic documentation

---

## Quick Start Commands

```bash
# Setup
git clone https://github.com/eece-4081-fall-2025/sara_howell_todo.git
cd sara_howell_todo
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate

# Development
python manage.py runserver  # Start server at http://127.0.0.1:8000/

# Testing
python manage.py test              # Run all tests
python manage.py test --verbosity=2  # Verbose output

# Database
python manage.py makemigrations    # Create migrations
python manage.py migrate           # Apply migrations
python manage.py createsuperuser   # Create admin user

# Admin
# Visit http://127.0.0.1:8000/admin/ after creating superuser
```

---

*Last Updated: September 2025*  
*README Version: 1.1*  
*Project Status: Active Development*