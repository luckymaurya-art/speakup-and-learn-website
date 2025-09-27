// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // CTA button smooth scrolling
    const ctaButtons = document.querySelectorAll('.cta-button');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (this.getAttribute('href') === '#download') {
                e.preventDefault();
                const downloadSection = document.querySelector('#download');
                if (downloadSection) {
                    downloadSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });

    // Navbar background change on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }
    });

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Animate elements on scroll
    const animateElements = document.querySelectorAll('.feature-card, .testimonial-card, .step');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Counter animation for hero stats
    const statNumbers = document.querySelectorAll('.stat-number');
    const animateCounters = () => {
        statNumbers.forEach(stat => {
            const target = parseInt(stat.textContent.replace(/[^\d]/g, ''));
            const suffix = stat.textContent.replace(/[\d]/g, '');
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    stat.textContent = target + suffix;
                    clearInterval(timer);
                } else {
                    stat.textContent = Math.floor(current) + suffix;
                }
            }, 30);
        });
    };

    // Trigger counter animation when hero section is visible
    const heroObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                heroObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        heroObserver.observe(heroSection);
    }

    // Download button interactions
    const downloadButtons = document.querySelectorAll('.download-btn');
    downloadButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Add click animation
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);

            // Show download instructions if not already visible
            const instructions = document.querySelector('.download-instructions');
            if (instructions) {
                instructions.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Parallax effect for hero section
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        if (hero) {
            const rate = scrolled * -0.5;
            hero.style.transform = `translateY(${rate}px)`;
        }
    });

    // Add loading animation
    window.addEventListener('load', function() {
        document.body.style.opacity = '0';
        document.body.style.transition = 'opacity 0.5s ease';
        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    });

    // Mobile menu toggle (if needed in future)
    const createMobileMenu = () => {
        const nav = document.querySelector('.nav-container');
        const menuToggle = document.createElement('button');
        menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
        menuToggle.className = 'mobile-menu-toggle';
        menuToggle.style.display = 'none';
        
        // Add mobile menu styles
        const style = document.createElement('style');
        style.textContent = `
            @media (max-width: 768px) {
                .mobile-menu-toggle {
                    display: block !important;
                    background: none;
                    border: none;
                    font-size: 1.5rem;
                    color: #6366f1;
                    cursor: pointer;
                }
                .nav-menu {
                    display: none;
                    position: absolute;
                    top: 100%;
                    left: 0;
                    right: 0;
                    background: white;
                    flex-direction: column;
                    padding: 20px;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                }
                .nav-menu.active {
                    display: flex;
                }
            }
        `;
        document.head.appendChild(style);
        nav.appendChild(menuToggle);
        
        menuToggle.addEventListener('click', () => {
            const navMenu = document.querySelector('.nav-menu');
            navMenu.classList.toggle('active');
        });
    };

    // Initialize mobile menu
    createMobileMenu();

    // Add hover effects to feature cards
    const featureCards = document.querySelectorAll('.feature-card');
    featureCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Add typing animation to hero title
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const originalText = heroTitle.innerHTML;
        heroTitle.innerHTML = '';
        
        let i = 0;
        const typeWriter = () => {
            if (i < originalText.length) {
                heroTitle.innerHTML += originalText.charAt(i);
                i++;
                setTimeout(typeWriter, 50);
            }
        };
        
        // Start typing animation after a short delay
        setTimeout(typeWriter, 500);
    }

    // Add pulse animation to CTA buttons
    const ctaPrimary = document.querySelector('.cta-button.primary');
    if (ctaPrimary) {
        setInterval(() => {
            ctaPrimary.style.transform = 'scale(1.05)';
            setTimeout(() => {
                ctaPrimary.style.transform = 'scale(1)';
            }, 200);
        }, 3000);
    }

    // Add scroll progress indicator
    const createScrollProgress = () => {
        const progressBar = document.createElement('div');
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, #6366f1, #8b5cf6);
            z-index: 9999;
            transition: width 0.1s ease;
        `;
        document.body.appendChild(progressBar);
        
        window.addEventListener('scroll', () => {
            const scrollTop = window.pageYOffset;
            const docHeight = document.body.offsetHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            progressBar.style.width = scrollPercent + '%';
        });
    };
    
    createScrollProgress();

    // FAQ Accordion functionality
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach((item, index) => {
        const question = item.querySelector('.faq-question');
        
        const toggleFAQ = () => {
            const isActive = item.classList.contains('active');
            
            // Close all other FAQ items
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                    const otherQuestion = otherItem.querySelector('.faq-question');
                    otherQuestion.setAttribute('aria-expanded', 'false');
                }
            });
            
            // Toggle current item
            if (isActive) {
                item.classList.remove('active');
                question.setAttribute('aria-expanded', 'false');
            } else {
                item.classList.add('active');
                question.setAttribute('aria-expanded', 'true');
            }
        };
        
        question.addEventListener('click', toggleFAQ);
        
        // Keyboard navigation
        question.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleFAQ();
            }
        });
    });

    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const name = formData.get('name');
            const email = formData.get('email');
            const subject = formData.get('subject');
            const message = formData.get('message');
            
            // Simple validation
            if (!name || !email || !subject || !message) {
                showNotification('Please fill in all fields.', 'error');
                return;
            }
            
            // Simulate form submission
            const submitBtn = this.querySelector('.submit-btn');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
            submitBtn.disabled = true;
            
            setTimeout(() => {
                showNotification('Thank you! Your message has been sent successfully.', 'success');
                this.reset();
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
            }, 2000);
        });
    }

    // Demo button functionality
    const demoBtn = document.getElementById('demo-btn');
    if (demoBtn) {
        demoBtn.addEventListener('click', function(e) {
            e.preventDefault();
            showDemoModal();
        });
    }

    // Pricing card hover effects
    const pricingCards = document.querySelectorAll('.pricing-card');
    pricingCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            if (!this.classList.contains('featured')) {
                this.style.transform = 'translateY(0) scale(1)';
            } else {
                this.style.transform = 'scale(1.05)';
            }
        });
    });

    // Enhanced testimonial animations
    const testimonialCards = document.querySelectorAll('.testimonial-card');
    testimonialCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
        card.classList.add('fade-in-up');
    });

    // Loading animation improvements
    const createLoadingOverlay = () => {
        const overlay = document.createElement('div');
        overlay.id = 'loading-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            transition: opacity 0.5s ease;
        `;
        
        overlay.innerHTML = `
            <div style="text-align: center; color: white;">
                <div style="width: 50px; height: 50px; border: 3px solid rgba(255,255,255,0.3); border-top: 3px solid white; border-radius: 50%; animation: spin 1s linear infinite; margin: 0 auto 20px;"></div>
                <h3 style="margin: 0; font-size: 1.5rem;">Loading SpeakUp & Learn...</h3>
                <p style="margin: 10px 0 0; opacity: 0.8;">Preparing your speaking journey</p>
            </div>
        `;
        
        document.body.appendChild(overlay);
        
        // Add spin animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(style);
        
        return overlay;
    };

    // Show loading overlay on page load
    const loadingOverlay = createLoadingOverlay();
    
    window.addEventListener('load', function() {
        setTimeout(() => {
            loadingOverlay.style.opacity = '0';
            setTimeout(() => {
                loadingOverlay.remove();
            }, 500);
        }, 1000);
    });

    // Notification system
    function showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            border-radius: 8px;
            color: white;
            font-weight: 600;
            z-index: 10000;
            transform: translateX(100%);
            transition: transform 0.3s ease;
            max-width: 300px;
        `;
        
        const colors = {
            success: '#10b981',
            error: '#ef4444',
            info: '#3b82f6',
            warning: '#f59e0b'
        };
        
        notification.style.background = colors[type] || colors.info;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Animate in
        setTimeout(() => {
            notification.style.transform = 'translateX(0)';
        }, 100);
        
        // Auto remove
        setTimeout(() => {
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 4000);
    }

    // Demo modal functionality
    function showDemoModal() {
        const modal = document.createElement('div');
        modal.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;
        
        modal.innerHTML = `
            <div style="background: white; border-radius: 15px; padding: 40px; max-width: 600px; width: 90%; text-align: center; transform: scale(0.9); transition: transform 0.3s ease;">
                <h2 style="margin-bottom: 20px; color: #1f2937;">Watch Our Demo</h2>
                <div style="background: #f3f4f6; border-radius: 10px; padding: 40px; margin: 20px 0;">
                    <i class="fas fa-play-circle" style="font-size: 4rem; color: #6366f1; margin-bottom: 20px;"></i>
                    <h3 style="color: #1f2937; margin-bottom: 10px;">Demo Video Coming Soon!</h3>
                    <p style="color: #64748b; margin-bottom: 20px;">We're working on an amazing demo video that will show you exactly how SpeakUp & Learn works.</p>
                    <p style="color: #6366f1; font-weight: 600;">In the meantime, download the app and try it yourself!</p>
                </div>
                <div style="display: flex; gap: 15px; justify-content: center; margin-top: 30px;">
                    <button onclick="this.closest('.modal').remove()" style="padding: 10px 20px; border: 2px solid #e5e7eb; background: white; border-radius: 8px; cursor: pointer; transition: all 0.3s ease;">Close</button>
                    <a href="#download" onclick="this.closest('.modal').remove()" style="padding: 10px 20px; background: #6366f1; color: white; text-decoration: none; border-radius: 8px; transition: all 0.3s ease;">Download App</a>
                </div>
            </div>
        `;
        
        modal.className = 'modal';
        document.body.appendChild(modal);
        
        // Animate in
        setTimeout(() => {
            modal.style.opacity = '1';
            modal.querySelector('div').style.transform = 'scale(1)';
        }, 100);
        
        // Close on background click
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                modal.remove();
            }
        });
    }

    // Enhanced scroll animations
    const createAdvancedScrollAnimations = () => {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, observerOptions);

        // Observe all sections
        const sections = document.querySelectorAll('section');
        sections.forEach(section => {
            section.classList.add('fade-in-up');
            observer.observe(section);
        });
    };

    createAdvancedScrollAnimations();

    // Add CSS for animations
    const animationStyles = document.createElement('style');
    animationStyles.textContent = `
        .fade-in-up {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .fade-in-up.animate-in {
            opacity: 1;
            transform: translateY(0);
        }
        
        .testimonial-card.fade-in-up {
            animation-delay: calc(var(--index) * 0.2s);
        }
    `;
    document.head.appendChild(animationStyles);
});
