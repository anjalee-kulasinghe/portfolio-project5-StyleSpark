# StyleSpark

## Code Institute - E-Commerce Applications Portfolio Project.

Find your perfect look for any occasion with StyleSpark party dress rental service. Choose from a wide range of stylish, high-quality dresses for all your events, and rent your favorite at a fraction of the retail price.

## Table of Contents

- [Project Structure](#project-structure)
- [Demo](#demo)
- [UX](#ux)
- [User Stories](#user-stories)
- [Strategy](#strategy)
- [Scope](#scope)
- [Structure](#structure)
- [Technologies](#technologies)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## Project Structure


## Demo

![Website look on different devices](media/readme-assets/device_look.PNG)

### Live Demo

A live demo of the website can be found [here](https://project5-stylespark-367466e38579.herokuapp.com/).

## UX

StyleSpark reimagines fashion by offering a curated selection of stunning dresses for rent. Look and feel your best for every occasion, all while embracing sustainable practices and keeping your budget happy.

Here's what makes the StyleSpark experience exceptional:

- Effortless Browsing:
  - A clean and intuitive interface lets you effortlessly browse our curated collection.
  - Filter by occasion to find your perfect match.
  - High-quality photos and detailed descriptions help you visualize the look.
- Seamless Rental Process:
  - Book your desired dress with just a few clicks.
  - Secure payment options ensure a smooth and worry-free transaction.
  - Clear instructions guide you through the rental process.
- Convenient Delivery & Returns:
  - Enjoy hassle-free delivery right to your doorstep.
  - Pre-paid return labels make sending the dress back a breeze.
- Premium Quality & Care:
  - Every dress is meticulously inspected, cleaned, and maintained to ensure pristine condition.
  - We provide detailed care instructions so you can look your best without worry.
  - Should any issue arise with the dress upon arrival, our responsive customer service is here to assist you.
- Sustainable Style:
  - Embrace fashion with a conscience.
  - Renting reduces fashion waste and promotes environmental responsibility.
  - Join the StyleSpark community and make a positive impact alongside looking fabulous.
- Affordable Luxury:
  - Access designer-worthy looks at a fraction of the cost of buying.
  - Refresh your wardrobe for every occasion without breaking the bank.
  - Experience the joy of high fashion without the hefty price tag.
- StyleSpark empowers you to:
  - Look and feel your absolute best for any event.
  - Experiment with different styles and discover your unique fashion voice.
  - Embrace sustainable practices and contribute to a greener future.

Get started with StyleSpark today and redefine the way you experience fashion!

## User Stories

As the developer of StyleSpark, I aimed to create a secure dress rental site that provides an intuitive and enjoyable experience for users and efficient management tools for administrators. Here are the user stories that outline the features and functionality of the platform:

### Customer Perspective

#### Browsing and Searching:

**User Story:**
As a user, I want to browse dresses by category (e.g., evening, cocktail, wedding) so that I can find dresses suitable for my event.

**Acceptance Criteria:**

- Users can see categories on the homepage.
- Clicking on a category displays dresses specific to that category.
- Users can filter dresses by size, color, and price within the category.

**User Story:**
As a user, I want to filter dresses by size, color, and price so that I can easily find a dress that meets my requirements.

**Acceptance Criteria:**

- Users can access filters on the browsing page.
- Applying filters updates the list of dresses displayed.
- Users can combine multiple filters (e.g., size and color).

**User Story:**
As a user, I want to search for dresses by keyword so that I can quickly locate specific styles or designers.

**Acceptance Criteria:**

- A search bar is available on the website.
- Entering a keyword and pressing search displays relevant results.
- Search results are accurate and relevant to the keyword.

#### Dress Details:

**User Story:**
As a user, I want to view detailed information about a dress (e.g., size guide, material, rental price, original price) so that I can make an informed decision.

**Acceptance Criteria:**

- Dress detail pages include size guide, material, rental price, and original price.
- Users can easily access the detailed information from the browsing page.

**User Story:**
As a user, I want to see high-quality images of the dress from multiple angles so that I can assess its appearance.

**Acceptance Criteria:**

- Dress detail pages include high-quality images.
- Images are available from multiple angles (front, back, side).
- Users can zoom in on images for a closer look.

#### Customer Reviews:

**User Story:**
As a user, I want to read reviews and ratings from other customers who have rented the dress so that I can measure its quality and fit.

**Acceptance Criteria:**

- Dress detail pages include customer reviews and ratings.
- Reviews are sortable by most recent, highest rating, and lowest rating.

**User Story:**
As a user, I want to leave a review after renting a dress so that I can share my experience with others.

**Acceptance Criteria:**

- Users can submit reviews only if they have rented the dress.
- Reviews include a star rating and a text comment.
- Submitted reviews are displayed on the dress detail page.

#### Rental Process:

**User Story:**
As a user, I want to select the rental duration (e.g., 4 days, 7 days) so that I can have the dress for the appropriate length of time.

**Acceptance Criteria:**

- Users can select rental duration options on the dress detail page.
- Rental price updates based on selected duration.
- Selected duration is reflected in the cart and checkout process.

**User Story:**
As a user, I want to add a dress to my cart and proceed to checkout so that I can complete my rental.

**Acceptance Criteria:**

- Users can add dresses to their cart.
- The cart displays selected dresses with rental details (duration, price).
- Users can proceed to checkout from the cart page.

#### Account Management:

**User Story:**
As a user, I want to create an account so that I can save my personal information and order history.

**Acceptance Criteria:**

- Users can create an account using email and password.
- Account creation is confirmed via email.
- Users can view and manage their personal information and order history.

**User Story:**
As a user, I want to log in to my account so that I can view and manage my rentals.

**Acceptance Criteria:**

- Users can log in using email and password.
- Logged-in users can access their account dashboard.
- The dashboard includes order history and rental details.

#### Payment and Delivery/Pickup:

**User Story:**
As a user, I want to choose my preferred payment method (e.g., credit card, PayPal) so that I can pay for my rental securely.

**Acceptance Criteria:**

- Users can select from multiple payment methods at checkout.
- Payment processing is secure and confirms successful transactions.
- Users receive a confirmation email upon successful payment.

**User Story:**
As a user, I want to provide a delivery address so that the dress can be shipped to me.

**Acceptance Criteria:**

- Users can enter and save a delivery address during checkout.
- The delivery address is confirmed before placing the order.
- Users receive tracking information once the dress is shipped.

**User Story:**
As a user, I want to track my order so that I can know when to expect delivery.

**Acceptance Criteria:**

- Users receive a tracking number once the dress is shipped.
- Users can access order tracking from their account dashboard.
- Tracking information is updated in real-time.

**User Story:**
As a user, I want to get details of the pickup location so that I can come and pick up my order.

**Acceptance Criteria:**

- Users receive a pickup location address.
- Pickup options are available for different times and dates.

#### Returns:

**User Story:**
As a user, I want to receive instructions on how to return the dress so that I can send it back easily.

**Acceptance Criteria:**

- Return instructions are provided with the dress delivery.
- Instructions are also available in the user’s account dashboard.
- Return packaging and shipping labels are included.

**User Story:**
As a user, I want to schedule a return pickup so that I don’t have to worry about shipping the dress back myself.

**Acceptance Criteria:**

- Users can schedule a return pickup from their account dashboard.
- Pickup options are available for different times and dates.
- Users receive confirmation for the scheduled pickup.

### Admin/Owner Perspective

#### Inventory Management:

**User Story:**
As an admin, I want to add new dresses to the inventory so that they are available for rental.

**Acceptance Criteria:**

- Admins can add dresses with all necessary details (images, sizes, prices).
- New dresses appear in the relevant categories for customers.
- Inventory is updated in real-time.

**User Story:**
As an admin, I want to update dress details (e.g., availability, rental price) so that the information is accurate.

**Acceptance Criteria:**

- Admins can edit existing dress details.
- Changes are reflected immediately on the website.
- Customers are notified of significant updates (e.g., price changes).

**User Story:**
As an admin, I want to remove dresses from the inventory so that they are no longer available for rental.

**Acceptance Criteria:**

- Admins can mark dresses as unavailable or remove them completely.
- Removed dresses no longer appear in customer searches or categories.
- Inventory reflects the updated status.

#### Order Management:

**User Story:**
As an admin, I want to view and manage customer orders so that I can ensure timely processing and delivery.

**Acceptance Criteria:**

- Admins can access a dashboard with all customer orders.
- Orders can be filtered by status (e.g., pending, shipped, returned).
- Admins can update order statuses and add tracking information.

**User Story:**
As an admin, I want to track the status of returned dresses so that I can update the inventory accordingly.

**Acceptance Criteria:**

- Admins can see a list of returned dresses.
- Return status is updated once the dress is inspected.
- Inventory is adjusted based on the condition of returned dresses.

#### Customer Support:

**User Story:**
As an admin, I want to respond to customer inquiries and issues so that I can provide excellent service.

**Acceptance Criteria:**

- Admins can access and respond to customer support tickets.
- Response times are tracked and reported.
- Customers receive notifications when their inquiries are addressed.

**User Story:**
As an admin, I want to manage customer reviews and feedback so that I can address any concerns.

**Acceptance Criteria:**

- Admins can view and moderate customer reviews.
- Inappropriate or spam reviews can be flagged and removed.
- Admins can respond to reviews directly to resolve issues.

#### Analytics and Reporting:

**User Story:**
As an admin, I want to view reports on rental trends and customer behavior so that I can make informed business decisions.

**Acceptance Criteria:**

- Admins can access detailed analytics and reports on rentals.
- Reports include data on popular dresses, rental durations, and customer demographics.
- Analytics can be exported for further analysis.

**User Story:**
As an admin, I want to analyze the performance of different dresses so that I can optimize the inventory.

**Acceptance Criteria:**

- Admins can view performance metrics for each dress (e.g., rental frequency, customer ratings).
- Data is updated in real-time and presented in a user-friendly format.
- Insights from performance data are actionable and help in inventory decisions.

### Strategy

Our strategy focuses on delivering a seamless and enjoyable experience for both customers and administrators, ensuring a robust and efficient dress rental platform. Key components of our strategy include:

#### Customer Experience
Enhanced Browsing and Searching: We prioritize intuitive browsing and searching functionalities, allowing customers to easily find dresses by category, and different sorting methods such as price. Our goal is to make the shopping experience effortless and tailored to individual preferences.

#### Detailed Dress Information: 
Providing comprehensive details such as size guides, materials, rental prices, and original prices ensures customers can make informed decisions. High-quality images from multiple angles enhance transparency and trust in the rental process.

#### Customer Reviews and Ratings: 
We encourage customer feedback through reviews and ratings, enabling prospective renters to gauge dress quality and fit based on real experiences. Sorting options by date and rating help users find the most relevant feedback quickly.

#### Efficient Rental Process: 
Simplifying the rental process with clear options for rental duration, straightforward checkout, and convenient return procedures ensures a hassle-free experience from start to finish.

#### Account Management: 
Secure account creation, easy login, and personalized dashboards empower customers to manage their orders, rentals, and personal information effortlessly.

#### Admin/Owner Operations Efficient Inventory Management: 
Our system supports admins in adding, updating, and removing dresses seamlessly. Real-time updates ensure inventory accuracy, while notifications for significant changes keep customers informed.

#### Order Management: 
Admins can efficiently handle orders with a centralized dashboard, filtering by status and updating order progress with tracking information. This ensures timely processing and delivery of rentals.

#### Customer Support and Reviews Management: 
We prioritize responsive customer support, managing inquiries, and addressing issues promptly. Admin tools for reviewing and moderating customer feedback help maintain service quality and resolve concerns effectively.

#### Continuous Improvement
- Feedback Loop: Regularly gathering and analyzing user feedback allows us to continuously improve our platform. Iterative updates and feature enhancements ensure we meet evolving customer needs and industry standards.

- Security and Reliability: Upholding robust security measures and ensuring platform reliability are fundamental to maintaining customer trust and data integrity.

### Scope

#### Purpose
The purpose of the dress rental platform is to provide customers with a convenient and enjoyable way to rent dresses for various occasions, while offering administrators robust tools for managing inventory, orders, customer interactions, and business analytics.

#### Features and Functionality

##### Customer-Facing Features

1. **Browsing and Searching**
   - Users can browse dresses by categories such as evening wear, cocktail dresses, and wedding attire.
   - Filtering options by size, color, and price are available to help users find dresses that meet their preferences.
   - A search functionality allows users to quickly locate specific dresses by entering keywords.

2. **Dress Details**
   - Each dress listing includes comprehensive information such as size guides, materials, rental prices, and original prices.
   - High-quality images from multiple angles (front, back, side) provide a detailed view of each dress.

3. **Customer Reviews and Ratings**
   - Users can read and contribute reviews and ratings based on their rental experiences.
   - Reviews are sortable by date and rating to help users make informed decisions.

4. **Rental Process**
   - Users can select rental durations (e.g., 4 days, 7 days) and view updated rental prices accordingly.
   - A streamlined checkout process allows users to add dresses to their cart and complete the rental transaction.

5. **Account Management**
   - Users can create accounts using email and password, enabling them to manage their personal information, order history, and rentals.
   - A personalized dashboard provides users with an overview of their account activities and settings.

6. **Payment and Delivery/Pickup**
   - Multiple secure payment options (e.g., credit card, PayPal) are available at checkout.
   - Users can provide delivery addresses for dress shipment or select pickup options for local availability.

7. **Order Tracking and Management**
   - Users receive tracking information for shipped dresses and can monitor order statuses through their account dashboard.
   - The platform provides users with details for scheduled pickup locations and times.

8. **Return Process**
   - Detailed instructions for returning dresses, including packaging and shipping labels, are accessible through the platform.
   - Users can schedule return pickups for added convenience.

##### Admin-Facing Features

1. **Inventory Management**
   - Admins can add new dresses to the inventory with detailed specifications and images.
   - Updates to dress availability and rental prices are reflected in real-time across the platform.

2. **Order Management**
   - A centralized dashboard allows admins to view and manage customer orders, including order status updates and tracking information.
   - Filtering options by order status (e.g., pending, shipped, returned) streamline order handling.

3. **Customer Support**
   - Admins can respond to customer inquiries and support tickets promptly through dedicated tools.
   - Tools for moderating customer reviews help maintain service quality and address customer concerns effectively.

4. **Analytics and Reporting**
   - Admins have access to comprehensive analytics and reports on rental trends, customer behavior, and dress performance.
   - Reporting tools enable admins to derive actionable insights for optimizing inventory management and business strategies.


### Structure

### 1. URLs (`urls.py`)

- **/about/**: About page providing information about the project.
- **/cart/**: Shopping cart for adding dresses and proceeding to checkout.
  - **/cart/add/{dress_id}/**: Add a dress to the cart.
  - **/cart/remove/{dress_id}/**: Remove a dress from the cart.
- **/checkout/**: Handles the checkout process including rental duration selection, payment method, and delivery/pickup details.
  - **/checkout/success/**: Success page after completing the checkout process.
- **/home/**: Homepage displaying featured dresses, categories, and search functionality.
- **/media/**: Media files such as dress images.
- **/products/**: Displays available dresses with filtering options.
  - **/products/{category_id}/**: Dresses filtered by a specific category.
  - **/products/detail/{dress_id}/**: Detailed view of a specific dress including images, description, size guide, rental price, and original price.
- **/profiles/**: User profiles and management.
  - **/profiles/{user_id}/**: Profile page for a specific user.
- **/static/**: Static files like CSS and JavaScript.
- **/admin/**: Admin dashboard for managing inventory, orders, and customer support.
  - **/admin/inventory/**: Inventory management.
    - **/admin/inventory/add/**: Form to add a new dress including details and images.
    - **/admin/inventory/edit/{dress_id}/**: Form to edit existing dress details.
    - **/admin/inventory/remove/{dress_id}/**: Remove a dress from inventory.
  - **/admin/orders/**: Order management.
    - **/admin/orders/all/**: List of all orders with filtering and status update options.
    - **/admin/orders/detail/{order_id}/**: Detailed view of a specific order with customer details, dress rented, status, and tracking information.

### 2. Views (`views.py`)

- **AboutView**: Renders the about page providing information about the project.
- **CartView**: Manages the shopping cart, allowing users to add, remove dresses, and proceed to checkout.
- **CheckoutView**: Handles the checkout process including rental duration selection, payment method, and delivery/pickup details.
- **HomeView**: Renders the homepage with featured dresses, categories, and search functionality.
- **ProductListView**: Displays a list of dresses with filtering options based on category, size, color, and price.
- **ProductDetailView**: Shows detailed information about a specific dress including images, description, size guide, rental price, and original price.
- **ProfileView**: Handles user profiles and displays user-specific information.
- **AdminDashboardView**: Provides an admin dashboard for managing inventory, orders, and customer support.
- **InventoryManagementView**: Handles adding, editing, and removing dresses from the inventory.
- **OrderManagementView**: Manages order processing, status updates, and tracking information.

### 3. Templates (`templates/`)

- **base.html**: Base template providing the common structure for all pages.
- **about.html**: Template for the about page providing information about the project.
- **cart.html**: Template for managing the shopping cart, adding, removing dresses, and proceeding to checkout.
- **checkout.html**: Template for the checkout process including rental duration selection, payment method, and delivery/pickup details.
- **checkout_success.html**: Template displayed upon successful completion of the checkout process.
- **index.html**: Template for the homepage displaying featured dresses, categories, and search functionality.
- **product_list.html**: Template for displaying a list of dresses with filtering options.
- **product_detail.html**: Template for showing detailed information about a specific dress.
- **profile.html**: Template for displaying user profile information.
- **admin_dashboard.html**: Template for the admin dashboard managing inventory, orders, and customer support.
- **inventory_management.html**: Template for managing inventory, adding, editing, and removing dresses.
- **order_management.html**: Template for managing order processing, status updates, and tracking information.


### 4. Models (`models.py`)

- **User**: Model for storing user information including email, password, and profile details.
- **Dress**: Model for storing dress information such as category, size, color, rental price, original price, and availability.
- **Order**: Model for tracking orders including customer details, dress rented, rental duration, status, and tracking information.

### 5. Forms (`forms.py`)

- **UserRegistrationForm**: Form for user registration and account creation.
- **UserLoginForm**: Form for user login and authentication.
- **CartForm**: Form for managing the shopping cart, adding, removing dresses, and proceeding to checkout.
- **CheckoutForm**: Form for handling the checkout process including rental duration selection, payment method, and delivery/pickup details.

### 6. Settings (`settings.py`)

- Configuration settings for Django including database connection, static files, templates, authentication, security, and installed apps.


### Technologies

- HTML
- CSS
- Django Python
- Heroku
- Balsamiq

### Features

#### Existing Features

- Navigation Bar: Provides easy access to different sections of the site, including Home, Products, Cart, Checkout, Profiles, and other relevant pages.
- Home: Introduces users to StyleSpark's party dress rental service, showcasing its offerings and inviting users to explore further.
- Cart: Allows users to manage their selected items before checkout, providing a summary and options for modification.
- Checkout: Guides users through the payment process for renting dresses, ensuring a seamless transaction experience.
- Products: Displays a range of stylish dresses available for rent, categorized and detailed to assist users in making selections.
  - Categorization:
    - Categories: Dresses are categorized based on types such as cocktail dresses, new arrivals, etc., facilitating easy browsing according to user preferences.
    - Tags: Products may be tagged with attributes like color, size, material, occasion (e.g., wedding, party), helping users refine searches and find specific items quickly.
- Search: Enables users to find specific blog posts or products by entering keywords, enhancing usability and navigation efficiency.
- Sign Up, Sign In, Logout: Provides essential user authentication functionalities, allowing new users to register, existing users to log in securely, and all users to log out when necessary.
- Admin Functionality: Empowers administrators to manage user accounts, oversee product listings, and monitor site activity effectively.
- Sorting: Enables users to arrange products or search results based on relevant criteria such as price, popularity, or category.
- Filtering: Allows users to narrow down product listings or search results based on specific attributes or preferences.
- Responsive Design: Ensures optimal viewing and interaction experience across a wide range of devices, enhancing accessibility and usability.


#### Features Left to Implement

- Edit Profile Page: Allow users to edit their profiles.
- Add more images: Enable users to see the different views of the dress.

## Testing

1) Responsive Design Testing:
    - Chrome DevTools:
      - Open your website in Chrome.
      - Right-click and select "Inspect" or press Ctrl+Shift+I.
      - Click the "Toggle device toolbar" button (or press Ctrl+Shift+M).
      - Select various devices from the dropdown list or enter custom dimensions.
      - Ensure the layout adjusts correctly for all screen sizes.
    - Manual Testing:
      - Manually test your application on different physical devices if available, like the Samsung Galaxy S23 Ultra.
2) Cross-Browser Testing:
    - Chrome:
      Open the website and check all functionalities.
    - Firefox:
      Repeat the same steps as in Chrome.
      Check if there are any specific issues related to Firefox.
    - Brave:
      Follow the same process to ensure Brave compatibility.
    - Edge:
      Follow the same process to ensure Edge compatibility.
3) Functional Testing:
    - Forms:
      - Ensure all form fields accept input as expected.
      - Test form validation (both client-side and server-side).
      - Verify successful form submissions and error handling
4) User Management:
      - User Registration:
        - Test user sign-up processes, including email verification if applicable.
      - User Login:
        - Verify login functionality with correct and incorrect credentials.
      - Password Management:
        - Test password reset and change features.
      - Role-Based Access Control:
        - Ensure users have appropriate access based on their roles.
5) Content Creation Features:
      - Content Addition:
        - Test adding new content as different user roles.
      - Content Editing:
        - Verify that content can be edited and changes are reflected appropriately.
      - Content Deletion:
        - Ensure that content deletion works and is irreversible if intended.
6) Additional Testing:
    - Performance Testing:
      - Use tools like Lighthouse to check performance, accessibility, and SEO.
    - Security Testing:
      - Conduct basic security testing to check for vulnerabilities like SQL injection.

## Deployment

This project was deployed using Heroku. Clone the repository, create a new Heroku app, link it to GitHub, and click Deploy.

## Credits

### Content

- Main code was taken from the Code Institute's [Boutique_ado_v1](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/master) project.
- Stack Overflow for error handling tips.
- Bootstrap for layout and navigation components.

### Media

- Images from Zalendo.se, Pixabay and Pexels.

### Acknowledgements

- Code Institute Building an E-Commerce Platform
- Code Institute Tutor Support Team.
- Mentor: Medale Oluwafemi.
- Grammar and spelling corrections using quillbot.com.
