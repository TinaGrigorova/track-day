
# 📘 Track Day

**Track Day** is a Django-based full-stack web application for motorsport enthusiasts to book and manage their track day experiences at popular UK circuits like Brands Hatch, Silverstone, and Lydden Hill. Users can choose available cars, time slots, and ride options (e.g. with/without instructor), and view or edit their bookings.

## 🔗 Live Demo

[Track Day App](https://track-day-b7bd1e661185.herokuapp.com)

[GitHub Repository](https://github.com/TinaGrigorova/track-day)

---

## 📸 Screenshots

- **Homepage** – With featured tracks  
  `booking_system/images/screenshot-homepage.png`

- **All Tracks** – Grid layout with track info and "Book Track" buttons  
  `booking_system/images/screenshot-tracks.png`

- **Booking Form** – Includes date, time, car, and ride options  
  `booking_system/images/screenshot-booking-form.png`

- **My Bookings** – User view of their current reservations  
  `booking_system/images/screenshot-my-bookings.png`

---

## 💡 Features

- 🛤 Browse and learn more about UK tracks.
- 🏎 Select and book a track with time and ride options.
- 👤 Secure user authentication (register/login/logout).
- ✍️ View, edit, or cancel bookings.
- 🚫 Prevent double-booking on the same track, time, and date.
- ✅ Admin interface to manage tracks, cars, and bookings.
- 🔐 Protected views for booking and user access.

---

## 🛠️ Technologies Used

| Type            | Stack                            |
|-----------------|----------------------------------|
| Frontend        | HTML5, CSS3, Bootstrap 5         |
| Backend         | Python 3.12, Django 4.2.1        |
| Database        | PostgreSQL                       |
| Authentication  | Django built-in Auth             |
| Hosting         | Heroku                           |
| Version Control | Git, GitHub                      |

---

## 🧪 Testing

Testing was performed manually and via Django’s built-in testing tools.

- Form validation for date and time
- Duplicate booking prevention
- Login/logout/signup processes
- Mobile responsiveness
- Booking updates/cancellation

➡️ See full documentation: [`TESTING.md`](TESTING.md)

---

## 👩‍💻 Developer Info

- Developed by: Tina Grigorova  
- Mentor: Mitko Bachvarov

---

## 🚀 Deployment

- Hosted on [Heroku](https://track-day-b7bd1e661185.herokuapp.com)
- Configure `DATABASE_URL` and `SECRET_KEY` as environment variables
- Use `gunicorn` for production and `whitenoise` for static files
- Collect static files: `python manage.py collectstatic`

---

## 📌 Future Enhancements

- Stripe integration for paid bookings
- Track day gift cards
- Admin calendar for track slot availability
- Booking confirmation email

---

## 📑 User Stories

- As a **user**, I want to browse tracks with pictures and info, so I can pick one I like.
- As a **logged-in user**, I want to book a track with specific date and time, so I can plan my experience.
- As a **user**, I want to edit or cancel my booking in case of a change in plans.
