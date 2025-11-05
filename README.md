# Simple Todo App
Todo app created in Django for EECE 4081!

## Development Stack
- Framework: Django
- Programming Language: Python 3.12.0
- IDE: Visual Studio Code
- Database: SQLite
- Virtual Environment: venv
- Version Control: Git
- Repository Hosting: GitHub
# Django Todo App - Core Task Creation Epic

A comprehensive Django-based todo application with advanced task management features including status tracking, date-based organization, and full CRUD operations. Built as part of EECE 4081 Software Engineering coursework.

**Student**: Sara Howell  
**Course**: EECE 4081 - Fall 2025  
**Repository**: https://github.com/eece-4081-fall-2025/sara_howell_todo

---

## Table of Contents

- [Features](#features)
- [Development Stack](#development-stack)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage Guide](#usage-guide)
- [Architecture and Design](#architecture-and-design)
- [Testing](#testing)
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
   - Automatic timestamp tracking (created_at, updated_at)

2. **Status Management**
   - Three-state status system: Pending, Done, Skipped
   - Visual indicators for each status
   - One-click status updates
   - Undo functionality to revert status changes

3. **Task Editing**
   - Full edit capabilities for all task attributes
   - Edit tasks from any time period (past, present, future)
   - Confirmation dialogs for destructive actions
   - Real-time validation

4. **Task Deletion**
   - Confirmation-based deletion to prevent accidents
   - Permanent removal with user acknowledgment

5. **Smart Organization**
   - Automatic categorization by date:
     - 🚨 Overdue Tasks (past due, still pending)
     - 📅 Today's Tasks (due today)
     - 🔮 Upcoming Tasks (future due dates)
     - 📋 Tasks Without Due Dates
   - Color-coded visual organization
   - Automatic sorting by due date and creation time

6. **Overdue Detection**
   - Computed `is_overdue` property on model
   - Only marks pending tasks as overdue
   - Completed/skipped tasks ignore due dates

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

### Key Django Components Used
- Models with choices and computed properties
- Class-based and function-based views
- Django Messages framework for user feedback
- Django Forms with custom widgets
- URL routing with named patterns
- Template inheritance and includes

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
│   │   └── 0001_initial.py
│   │
│   ├── templates/                # HTML templates
│   │   └── todo/
│   │       ├── todo_list.html           # Main task list view
│   │       ├── todo_form.html           # Create/Edit form
│   │       └── todo_confirm_delete.html # Delete confirmation
│   │
│   ├── __init__.py
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # App configuration
│   ├── models.py                 # Data models (ToDo)
│   ├── views.py                  # View functions
│   ├── urls.py                   # App URL patterns
│   ├── forms.py                  # Form definitions
│   └── tests.py                  # Test suite
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

---

## Usage Guide

### Creating Tasks

**Quick Add (Homepage):**
1. Enter task description in the "What needs to be done?" field
2. Optionally select a due date
3. Click "Add Task"
4. Task is created with default "Pending" status

**Detailed Creation:**
1. Click "Create Task" or navigate to `/create/`
2. Fill in task details:
   - Task name (required)
   - Due date (optional)
   - Status (Pending/Done/Skipped)
3. Click "Create Task"

### Managing Task Status

**Mark as Done:**
- Click the green "✓ Done" button on any pending task
- Task moves to completed state with visual strikethrough

**Mark as Skipped:**
- Click the gray "⊘ Skip" button on any pending task
- Task is marked skipped and visually de-emphasized

**Undo Status:**
- Click the yellow "↺ Undo" button on completed/skipped tasks
- Task returns to pending status

### Editing Tasks

1. Click the "✎ Edit" button on any task
2. Modify any field (name, due date, status)
3. Click "Edit Task" to save changes
4. Or click "Cancel" to discard changes

**Note**: You can edit tasks from any time period - past, present, or future.

### Deleting Tasks

1. Click the red "✗ Delete" button on any task
2. Review the confirmation page showing task details
3. Click "Yes, Delete It" to permanently remove
4. Or click "Cancel" to return without deleting

### Viewing Organized Tasks

Tasks are automatically organized into sections:

- **Overdue Tasks**: Past due date, still pending (red indicator)
- **Today's Tasks**: Due today (green indicator)
- **Upcoming Tasks**: Future due dates (blue indicator)
- **No Due Date**: Tasks without assigned dates

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
    
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Key Design Decisions:**
- Used `CharField` with choices for status (extensible, database-efficient)
- Separated creation and update timestamps for audit trail
- Made due_date optional for flexibility
- Added `is_overdue` computed property for business logic
- Implemented custom ordering by due date, then creation time

### View Architecture

**Function-Based Views** for simplicity and clarity:

- `todo_list`: Main view with date-based organization and quick add
- `todo_create`: Detailed task creation form
- `todo_edit`: Task modification with pre-populated data
- `todo_delete`: Confirmation-based deletion
- `todo_mark_done/skipped/pending`: Single-purpose status updates

**Design Pattern**: Each view follows Django best practices:
- GET requests display forms/data
- POST requests process form submissions
- Redirects after successful POST (PRG pattern)
- User feedback via Django Messages framework

### Form Design

**Two-Form Strategy:**

1. **QuickAddForm**: Minimal fields for rapid task entry
   - Name (required)
   - Due date (optional)
   - Auto-sets status to "pending"

2. **TodoForm**: Complete task management
   - Name (required)
   - Due date (optional)
   - Status (required, with all choices)

**Benefits**: Optimized UX for different use cases without form duplication.

### Template Design

**Inheritance Structure:**
- Self-contained templates (no base template yet)
- Inline CSS for simplicity
- Responsive design with modern gradients
- Consistent color scheme:
  - Purple/blue gradients for headers
  - Yellow for pending tasks
  - Green for completed tasks
  - Gray for skipped tasks
  - Red for overdue warnings

---

## Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific test class
python manage.py test todo.tests.ToDoModelTests

# Run with verbose output
python manage.py test --verbosity=2

# Run with coverage (if coverage.py installed)
coverage run --source='.' manage.py test
coverage report
```

### Test Coverage

**Model Tests** (`ToDoModelTests`):
- Basic CRUD operations
- String representation
- Default values
- Status choices validation
- Due date handling
- `is_overdue` property (all edge cases)
- Timestamp functionality
- Custom ordering

**Form Tests** (`TodoFormTests`, `QuickAddFormTests`):
- Valid data submission
- Required field validation
- Optional field handling
- Invalid status handling

**View Tests** (`TodoViewTests`):
- All CRUD endpoints
- GET and POST requests
- Status transitions
- Date-based organization
- Redirect behavior
- 404 handling
- Template usage

**Integration Tests** (`TodoIntegrationTests`):
- Complete task lifecycle
- Date filtering accuracy
- Multiple tasks handling
- Real-world workflows

**Total Test Count**: 40+ comprehensive tests

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
| `/admin/` | Django Admin | ALL | Admin interface |

**RESTful Principles:**
- Clear, semantic URL patterns
- Appropriate HTTP methods
- Resource-based naming
- Predictable endpoints

---

## Database Schema

### ToDo Table

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Integer | Primary Key, Auto-increment | Unique identifier |
| name | CharField(255) | NOT NULL | Task description |
| status | CharField(10) | NOT NULL, Choices | Current status |
| due_date | DateField | NULL, BLANK | Optional deadline |
| created_at | DateTimeField | NOT NULL, Auto-add | Creation timestamp |
| updated_at | DateTimeField | NOT NULL, Auto-update | Last modification |

**Indexes:**
- Primary key on `id`
- Ordering index on `(due_date, -created_at)`

**Constraints:**
- `status` must be in ['pending', 'done', 'skipped']
- `name` max length 255 characters

---

## Future Enhancements

### Planned Features (Sprint 2+)

1. **Task Priorities**
   - High/Medium/Low priority levels
   - Visual indicators
   - Priority-based sorting

2. **Task Categories/Tags**
   - Categorization system
   - Filtering by category
   - Tag-based organization

3. **User Authentication**
   - Multi-user support
   - Personal task lists
   - User permissions

4. **Recurring Tasks**
   - Daily/Weekly/Monthly recurrence
   - Auto-creation of recurring instances
   - Recurrence pattern management

5. **Search and Filters**
   - Full-text search
   - Advanced filtering options
   - Saved filter presets

6. **Notifications**
   - Due date reminders
   - Overdue notifications
   - Email integration

7. **Task Notes/Comments**
   - Detailed task descriptions
   - Comment system
   - Attachment support

8. **Statistics Dashboard**
   - Completion rates
   - Productivity analytics
   - Visual charts and graphs

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

### Code Quality

- Clean, maintainable code following PEP 8
- Comprehensive docstrings for all functions
- Proper error handling with user feedback
- Separation of concerns (models, views, forms, templates)
- DRY principles applied throughout

### Performance Considerations

- Efficient database queries
- Proper use of Django ORM
- Minimal template logic
- Future consideration: Query optimization with select_related/prefetch_related

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

## Version History

### Version 1.0
- Initial release
- Core CRUD operations
- Status management system
- Date-based organization
- Comprehensive test suite
- Full documentation