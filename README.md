# Delivery_Management_System

## 🚚 What is a Delivery Management System (DMS)?

A **Delivery Management System** helps businesses:
✅ Manage orders and deliveries.
✅ Track delivery status and delivery personnel.
✅ Optimize routes for deliveries.
✅ Notify customers about order and delivery status.
✅ Maintain records for analysis and reporting.

---

## 🛠️ Why use Python and Django?

**Python** offers:

* Readable, maintainable code.
* Powerful libraries (e.g., Pandas, NumPy, Requests).

**Django** offers:

* Built-in admin for managing deliveries.
* User authentication for delivery personnel and customers.
* REST API support for mobile app integration.
* ORM for database handling.
* Scalability and security.

---

## 🏗️ Typical Features in a DMS

1️⃣ **User Roles:**

* Admin (manage system, assign deliveries)
* Delivery Personnel (view assigned deliveries, update status)
* Customer (track order status)

2️⃣ **Order Management:**

* Create, update, and delete orders.
* Assign orders to delivery personnel.
* Set delivery status (pending, in-transit, delivered).

3️⃣ **Tracking and Notifications:**

* Track current status.
* Send notifications via email/SMS.

4️⃣ **Reporting:**

* Delivery success rates.
* Average delivery times.
* Pending deliveries.

---

## 🗂️ Basic Django Project Structure for DMS

```
delivery_project/
    manage.py
    delivery_project/
        settings.py
        urls.py
    delivery_app/
        models.py
        views.py
        urls.py
        templates/
        static/
```

---

## 🖥️ Key Components

### 1️⃣ Models (`models.py`)

Define:

* `Order` model:

  * `customer_name`, `address`, `order_details`, `status`, `assigned_to`.
* `DeliveryPersonnel` model:

  * `user`, `phone_number`, `availability_status`.

### 2️⃣ Views (`views.py`)

* `create_order` – For admin to create orders.
* `assign_order` – Assign orders to delivery personnel.
* `update_status` – Delivery personnel updates status.
* `track_order` – Customers view order status.

### 3️⃣ Templates

* Simple HTML pages for:

  * Order listing.
  * Delivery personnel dashboards.
  * Order tracking page for customers.

### 4️⃣ Admin Integration

Using Django Admin:

* Admin can add orders, view statuses, and manage delivery personnel without custom UIs initially.

---

## ⚡ Technologies you can integrate later:

✅ **Django REST Framework** for APIs (mobile app support).
✅ **Celery** for sending notifications automatically.
✅ **Map APIs (Google Maps API)** for route optimization.
✅ **QR code generation** for delivery confirmation scanning.

---

## 🚀 Advantages of building it using Django:

✅ Quick prototype using Django Admin.
✅ Secure user authentication and permissions.
✅ Can be scaled using DRF + React/Flutter frontend.
✅ Easy integration with SMS/Email APIs for notifications.

---

## ✅ Summary

A **Delivery Management System using Python and Django**:
🔹 Allows managing, tracking, and optimizing deliveries for businesses.
🔹 Uses Django’s models, views, templates, and admin for structured delivery management.
🔹 Supports scalable extensions like APIs, Celery tasks, and real-time tracking for advanced functionality.

---
## Screenshots
<img width="1501" alt="Screenshot 2025-06-29 at 12 07 57 AM" src="https://github.com/user-attachments/assets/b292114a-6553-4bcf-8c62-3efe9b9fc1d2" />

<img width="1501" alt="Screenshot 2025-06-29 at 12 08 04 AM" src="https://github.com/user-attachments/assets/2eae3eda-1c14-4792-8221-f43bb436fa89" />

<img width="1501" alt="Screenshot 2025-06-29 at 12 09 08 AM" src="https://github.com/user-attachments/assets/1bef531a-1fd1-4e09-9cab-90aefeee3c0c" />

<img width="1501" alt="Screenshot 2025-06-29 at 12 09 16 AM" src="https://github.com/user-attachments/assets/e837fc8f-8b0c-4530-accf-15ef2f01df9d" />

<img width="1501" alt="Screenshot 2025-06-29 at 12 10 53 AM" src="https://github.com/user-attachments/assets/71fff5eb-5360-447a-9d68-6ffd99b91c3e" />






<img width="1501" alt="Screenshot 2025-06-29 at 12 07 52 AM" src="https://github.com/user-attachments/assets/d8f0bf15-444f-4e1b-82fa-78ce829526ef" />

<img width="1501" alt="Screenshot 2025-06-29 at 12 07 45 AM" src="https://github.com/user-attachments/assets/696a378d-8bc2-471b-98e1-7e8e67bd1bc7" />

<img width="1501" alt="Screenshot 2025-06-29 at 12 07 29 AM" src="https://github.com/user-attachments/assets/0a754309-7090-41ad-baed-a061a3248679" />
