# TESTING.md – Track Day Booking

## Manual Testing

### ✅ Core Features Tested

#### 1. **User Registration & Login**
- Registered with valid email and password
- Logged in successfully
- Invalid login tested with appropriate error feedback

#### 2. **Booking a Track**
- User can choose a track, date, car, time, and ride option
- Booking confirmation displays success message
- Booking duplicates blocked by validation

#### 3. **View/Edit/Cancel Bookings**
- View bookings in a clean table
- Edit functionality pre-fills form
- Successfully updates all fields
- Booking cannot be edited to overlap an existing one

#### 4. **Error Pages**
- 404, 500, 403, and 400 error pages implemented with custom design

#### 5. **Authentication**
- Booking page is protected: redirects unauthenticated users to login

### ❌ Bugs Identified and Fixed

| Issue | Resolution |
|------|------------|
| Changing only ride option didn’t save | Adjusted form validation to allow same-time edits |
| Booking page accessible without login | Wrapped view in `@login_required` |
| Error pages weren’t rendering | Defined handlers in `urls.py` and created templates |

## Automated Testing (Planned)
- Coverage with `pytest-django`
- Model testing for Booking, Track, and Car
- Form validation tests

---

Tested across latest Chrome, Firefox, and Safari browsers. Responsive tests done with dev tools and real devices.
