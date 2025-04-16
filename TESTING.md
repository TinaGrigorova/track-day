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
