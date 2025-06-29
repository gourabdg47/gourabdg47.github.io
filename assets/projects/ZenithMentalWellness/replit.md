# Zenith Health - Men's Mental Health Awareness Platform

## Overview

Zenith Health is a single-page web application focused on men's mental health awareness and community support. The platform serves as a landing page to promote mental health resources and facilitate community engagement through Discord integration. Built with modern web technologies, it emphasizes accessibility, responsive design, and user engagement.

## System Architecture

The application follows a simple client-side architecture:

**Frontend-Only Architecture**: Pure HTML/CSS/JavaScript implementation without backend dependencies
- Single HTML file serving as the main entry point
- CSS for styling and animations
- Vanilla JavaScript for interactivity and user experience enhancements
- CDN-based dependencies for external libraries

**Design Philosophy**: 
- Mobile-first responsive design
- Dark theme with calming color palette
- Animated background elements for visual appeal
- Focus on accessibility and user experience

## Key Components

### 1. User Interface Layer
- **Main Layout**: Single-page application with sections for different content areas
- **Navigation System**: Mobile-responsive navigation with hamburger menu
- **Modal System**: JavaScript-powered modal functionality for enhanced user interactions
- **Animation System**: CSS-based floating orb animations and scroll-triggered animations

### 2. Styling Architecture
- **Framework**: Tailwind CSS via CDN for utility-first styling
- **Custom Theming**: Extended color palette focusing on calming, mental health-appropriate colors
  - Dark primary/secondary backgrounds
  - Calm blue and teal accent colors
  - Soft gray and warm white for text
- **Typography**: Inter font for body text, Poppins for headings
- **Icons**: Font Awesome integration for consistent iconography

### 3. Interactive Components
- **Mobile Menu**: Collapsible navigation for mobile devices
- **Smooth Scrolling**: Enhanced navigation experience
- **Modal Management**: Reusable modal system for various content overlays
- **Loading States**: Progressive enhancement with loading animations

## Data Flow

Since this is a static frontend application, data flow is primarily:

1. **User Interactions → JavaScript Event Handlers**
   - Navigation clicks trigger smooth scrolling
   - Mobile menu interactions toggle visibility states
   - Modal triggers manage overlay states

2. **Animation States → CSS Transitions**
   - Scroll position triggers animation states
   - Background orbs follow continuous animation loops
   - Loading states transition to active states

3. **External Integrations**
   - Discord community links (external navigation)
   - Font and icon CDN resources
   - Social media integrations (planned)

## External Dependencies

### CDN Dependencies
- **Tailwind CSS**: Utility-first CSS framework
- **Google Fonts**: Typography (Inter, Poppins)
- **Font Awesome**: Icon library
- **No JavaScript frameworks**: Vanilla JS approach for simplicity

### Third-party Integrations
- **Discord**: Community platform integration (external links)
- **Social Media**: Planned integrations for broader reach

## Deployment Strategy

**Static Site Deployment**: 
- Suitable for any static hosting platform (Netlify, Vercel, GitHub Pages, etc.)
- No server-side processing required
- CDN-optimized for global performance
- Mobile-responsive across all devices

**Advantages**:
- Fast loading times
- Minimal hosting costs
- Easy to maintain and update
- High availability and reliability

**Considerations**:
- Limited to client-side functionality
- No user data persistence without external services
- Future backend integration may be needed for advanced features

## Recent Changes

- **June 29, 2025 - Updated Design & Features**:
  - Changed from dark to light color theme for better accessibility
  - Improved header design with proper logo container and alignment
  - Simplified Discord button with clean styling and Discord logo
  - Added comprehensive footer with navigation links and crisis information
  - Enhanced background animations with 4 floating orbs and smoother movement
  - Added detailed Resources section with community support, mental health resources, and professional help information
  - Updated all color schemes to work with lighter theme (light-primary, light-secondary, text-primary, text-secondary)

## Changelog

- June 29, 2025. Initial setup and major design updates

## User Preferences

Preferred communication style: Simple, everyday language.