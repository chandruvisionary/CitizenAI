# CitizenAI - Government Services AI Assistant

## Overview

CitizenAI is a Flask-based web application that serves as an AI-powered chatbot for government services. The platform enables citizens to ask government-related questions and receive instant responses using IBM's Granite AI model via Hugging Face. The system also collects and analyzes user feedback through sentiment analysis to help improve public services and understand citizen satisfaction.

The application features user authentication, real-time chat functionality, sentiment analysis dashboard, and responsive web design. It's designed to bridge the communication gap between citizens and government institutions by making public services more accessible and user-friendly.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Web Framework Architecture
- **Framework**: Flask with SQLAlchemy ORM for database operations
- **Template Engine**: Jinja2 templates with HTML5 and custom CSS
- **Session Management**: Flask sessions with secure secret key configuration
- **Middleware**: ProxyFix for handling reverse proxy headers

### Database Design
- **Primary Database**: SQLite with SQLAlchemy ORM (configurable via environment variables)
- **Models**: 
  - User model for authentication with encrypted passwords
  - ChatHistory model for storing conversation logs
  - Feedback model for sentiment analysis data
- **Connection Management**: Pool recycling and pre-ping for connection reliability

### AI Integration Architecture
- **Primary AI Model**: IBM Granite 3.3-8b-instruct accessed via Hugging Face Inference API
- **Sentiment Analysis**: TextBlob library for natural language processing and sentiment classification
- **API Communication**: HTTP requests to Hugging Face endpoints with error handling

### Frontend Architecture
- **Design System**: Custom CSS with gradient backgrounds and card-based layouts
- **Responsive Design**: Mobile-first approach with flexible grid systems
- **Interactive Elements**: Chart.js for data visualization in dashboard
- **User Experience**: Progressive enhancement with fade-in animations

### Authentication & Security
- **Password Security**: Werkzeug password hashing with salt
- **Session Management**: Secure session cookies with configurable secret keys
- **User State**: Server-side session storage for authentication status
- **Input Validation**: Form validation for user inputs and data sanitization

### Data Flow Architecture
- **Chat Flow**: User question → AI API → Response storage → Feedback collection
- **Sentiment Pipeline**: Feedback text → TextBlob analysis → Dashboard aggregation
- **Dashboard Analytics**: Real-time sentiment statistics with visual charts

## External Dependencies

### AI Services
- **Hugging Face Inference API**: Primary AI model hosting and inference
  - Model: IBM Granite 3.3-8b-instruct
  - Authentication via HF_API_KEY environment variable
  - HTTP-based API communication

### Natural Language Processing
- **TextBlob**: Sentiment analysis and text processing
  - Automatic sentiment polarity detection
  - Classification into positive, neutral, negative categories

### Frontend Libraries
- **Chart.js**: Data visualization for sentiment analytics dashboard
  - Loaded via CDN for chart rendering
  - Interactive charts for feedback statistics

### Database Options
- **SQLite**: Default local database for development
- **PostgreSQL**: Production database option via DATABASE_URL environment variable
- **SQLAlchemy**: ORM layer for database abstraction

### Python Dependencies
- **Flask**: Web framework and routing
- **Flask-SQLAlchemy**: Database ORM integration
- **Werkzeug**: Security utilities and password hashing
- **Requests**: HTTP client for external API calls

### Environment Configuration
- **SESSION_SECRET**: Flask session encryption key
- **DATABASE_URL**: Database connection string
- **HF_API_KEY**: Hugging Face API authentication token
