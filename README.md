# Job Portal (Django Backend Project)

A **Job Portal Web Application** built with **Django** .  
The project demonstrates **custom user authentication, role-based access, job posting, and job applications**, designed with scalability and maintainability in mind.

---

## 🚀 Features 
- **Custom User Model**  
  - Extended Django’s AbstractUser to support `Job Seeker` and `Employer` roles.
  - Automatic creation of user profiles with default values on signup.

- **Authentication & Authorization**  
  - Secure login, signup, and logout flows.  
  - CSRF protection and session-based authentication.  
  - Custom logout redirection to `success_logout.html`.

- **Role-Based Access Control**  
  - Employers can post and manage jobs.  
  - Job seekers can apply for jobs.  
  - Conditional rendering (e.g., "Post Job" button visible only to Employers).

- **Job Applications**  
  - Users can apply for jobs.  
  - Application tracking per user (`job_app.job.title` in templates).

- **Database Models**  
  - **User** (custom model with roles).  
  - **UserProfile** (extended details, editable later).  
  - **Job** (title, description, employer relation).  
  - **JobApplication** (user → job mapping).

- **Error Handling & Debugging**   
  - Queryset debugging: learned how to access fields explicitly in templates.

---

## 🛠️ Tech Stack
- **Backend Framework**: Django (MVT pattern)  
- **Database**: SQLite (default, can be extended to PostgreSQL/MySQL)  
- **Authentication**: Django built-in auth (customized)  
- **Templates**: Django Template Language (DTL)  
- **Deployment**: Localhost / Configurable for production (Gunicorn + Nginx)

---

