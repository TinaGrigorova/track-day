# Track Day | Testing

Return to [README](README.md)
- - -
Comprehensive testing has been performed to ensure the website's seamless and optimal functionality.

## Responsiveness Testing

The Track Day website was meticulously tested across a variety of devices and screen sizes to ensure optimal responsiveness and user experience. Utilizing browser developer tools, such as Chrome DevTools, the site was evaluated in simulated environments representing smartphones, tablets, and desktops. This process allowed for real-time adjustments and ensured that the layout and functionality remained consistent across different viewports.​

<details>
<summary> Desktop PC
</summary>

![Desktop PC]()
</details>

<details>
<summary> Laptop
</summary>

![Laptop]()
</details>

<details>
<summary> Tablet
</summary>

![Tablet]()
</details>

<details>
<summary> Mobile
</summary>

![Mobile]()
</details>

## Browser Compatibility Testing

The Track Day website was rigorously tested across multiple web browsers to ensure consistent functionality and appearance. This testing process guarantees a smooth and uniform user experience, regardless of the browser used.​

<details>
<summary> Chrome
</summary>

![Chrome]()
</details>

<details>
<summary> Microsoft Edge
</summary>

![Microsoft Edge]()
</details>

<details>
<summary> Safari
</summary>

![Safari]()
</details>

<details>
<summary> Iphone Internet (Mobile)
</summary>

![Iphone Internet Mobile]()
</details>

## Device Testing

Device testing was conducted on a variety of phone models, including Iphone 11, Oppo, iPhone 14, Huawei. The assistance of family members and friends was sought to perform the testing. This comprehensive approach ensured that the website was thoroughly evaluated on different devices and platforms, contributing to a more robust and user-friendly final product.

---
## Code Validation

### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page]()
</details>


<details>
<summary> Sign Up Page
</summary>

![Sign Up Page]()
</details>

<details>
<summary> Login Page
</summary>
  
![Login Page]()
</details>

<details>
<summary> Make a Booking Page
</summary>

![Make a Booking Page]()
</details>

<details>
<summary> Booking Success Page
</summary>

![Booking Success Page]()
</details>

<details>
<summary> Booking Overview Page
</summary>

![Booking Overview Page]()
</details>

<details>
<summary> Edit Booking Page
</summary>
  
![Edit Booking Page]()
</details>

<details>
<summary> Delete Booking Page
</summary>

![Delete Booking Page]()
</details>

<details>
<summary> 404 Error Page
</summary>

![404 Error Page]()
</details>

<details>
<summary> 500 Error Page
</summary>

![500 Error Page]()
</details>

### CSS Validation

<details>
<summary> Custom CSS (style.css)
</summary>

![Custom CSS (style.css)]()
</details>

### Python

#### booking-system app

<details>
<summary> admin.py
</summary>

![admin.py]()
</details>

<details>
<summary> forms.py
</summary>

![forms.py]()
</details>

<details>
<summary> models.py
</summary>

![models.py]()
</details>

<details>
<summary> views.py
</summary>

![views.py]()
</details>

<details>
<summary> urls.py
</summary>

![urls.py]()
</details>

#### track-day App

<details>
<summary> settings.py
</summary>

![settings.py]()
</details>

<details>
<summary> urls.py
</summary>

![urls.py]()
</details>

## Lighthouse Report

<details>
<summary> Home Page
</summary>

![Home Page]()
</details>


<details>
<summary> Sign Up Page
</summary>

![Sign Up Page]()
</details>

<details>
<summary> Login Page
</summary>

![Login Page]()
</details>


<details>
<summary> All Tracks Page
</summary>

![Browse Tracks]()
</details>

<details>
<summary> Make a Booking Page
</summary>


![Booking Overview Page]()
</details>

<details>
<summary> Edit Booking Page
</summary>
  
![Edit Booking Page]()
</details>

<details>
<summary> Delete Booking Page
</summary>

![Delete Booking Page]()
</details>

## Bugs

### Resolved Bugs






## Features Testing
 
| Page                | User Action                                      | Expected Result                                              | Status |
|---------------------|--------------------------------------------------|---------------------------------------------------------------|--------|
| **Home Page**       | Click on Logo                                    | Redirect to Home Page                                        | ✅ PASS |
|                     | Click on Sign Up button                          | Redirect to Sign Up page                                     | ✅ PASS |
|                     | Click on Login                                   | Redirect to Login page                                       | ✅ PASS |
|                     | Click on a Track Card                            | Redirect to Track Detail page                                | ✅ PASS |
|                     | Click on "See All Tracks"                       | Redirect to All Tracks listing page                          | ✅ PASS |
|                     | Hover on Track Card                              | Card zooms and reveals full description                      | ✅ PASS |
|                     | Click on Book Track                              | Redirect to Book Track page                                  | ✅ PASS |
| **Sign Up Page**    | Fill invalid form                                | Displays validation errors                                   | ✅ PASS |
|                     | Submit valid form                                | Account created and redirected to homepage                   | ✅ PASS |
|                     | Click login link                                 | Redirect to login page                                       | ✅ PASS |
| **Login Page**      | Submit invalid credentials                       | Displays error message                                       | ✅ PASS |
|                     | Submit valid credentials                         | Redirect to homepage, user greeted                           | ✅ PASS |
|                     | Click sign up link                               | Redirect to signup page                                      | ✅ PASS |
| **Booking Page**    | Not logged in                                    | Redirected to login page                                     | ✅ PASS |
|                     | Submit empty form                                | Display validation errors                                    | ✅ PASS |
|                     | Select valid data                                | Booking successful, redirected to My Bookings                | ✅ PASS |
|                     | Try booking same track, date, time               | Validation error, can't double book                          | ✅ PASS |
| **My Bookings**     | View booking details                             | Details displayed in table                                   | ✅ PASS |
|                     | Click Edit                                       | Redirect to Edit Booking page                                | ✅ PASS |
|                     | Click Cancel                                     | Booking is deleted                                           | ✅ PASS |
| **Edit Booking**    | Change valid details and submit                  | Booking updates successfully                                 | ✅ PASS |
|                     | Only change ride/car option and submit           | Booking updates successfully                                 | ✅ PASS |
|                     | Submit conflicting time/date                     | Validation error                                              | ✅ PASS |
| **All Tracks**      | Hover card                                       | Show full description overlay                                | ✅ PASS |
|                     | Click Book Track                                 | Redirects to Book page with selhttps://github.com/TinaGrigorova/track-day/blob/main/TESTING.mdected track                   | ✅ PASS |
| **Track Detail Pages** | View track info                              | Track information and gallery loads                          | ✅ PASS |
|                     | Click Book this Track                            | Redirect to booking form                                     | ✅ PASS |
|                     | Click Back                                       | Returns to homepage                                          | ✅ PASS |
| **Error Pages**     | Type invalid URL                                 | Custom 404 page appears                                      | ✅ PASS |
|                     | Trigger error manually (dev)                     | Custom 500 page appears                                      | ✅ PASS |

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
