// Select the button, form, and overlay
const contactButton = document.getElementById('contactUsButton');
const contactForm = document.getElementById('contact-us');
const overlay = document.getElementById('overlay');
const closeButton = document.getElementById('closeForm');

// Add event listener to the "Contact Us" button
contactButton.addEventListener('click', function() {
    contactForm.style.display = 'flex';  // Show the contact form
    overlay.style.display = 'block';     // Show the overlay
});

// Add event listener to the "Close" button
closeButton.addEventListener('click', function() {
    contactForm.style.display = 'none';  // Hide the contact form
    overlay.style.display = 'none';      // Hide the overlay
});
 
