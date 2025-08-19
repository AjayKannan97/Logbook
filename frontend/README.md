# Logbook Frontend

A modern React-based frontend application for the Logbook customer management system.

## Features

- **Customer Management**: Add, view, and manage customer records
- **Payment Status Tracking**: Visual status indicators for payment tracking
- **Search Functionality**: Search customers across all fields in real-time
- **Responsive Design**: Modern, mobile-friendly user interface
- **Real-time Updates**: Instant feedback and data synchronization
- **Form Validation**: Client-side validation for better user experience

## Tech Stack

- **Framework**: React 18+ with modern hooks
- **Build Tool**: Vite for fast development and building
- **Styling**: Custom CSS with modern design principles
- **HTTP Client**: Axios for API communication
- **State Management**: React useState and useEffect hooks

## Prerequisites

- Node.js 16+ 
- npm or yarn package manager
- Modern web browser

## Installation

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

## Development

### Start Development Server
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

### Build for Production
```bash
npm run build
# or
yarn build
```

### Preview Production Build
```bash
npm run preview
# or
yarn preview
```

## Project Structure

```
frontend/
├── src/
│   ├── App.jsx          # Main application component
│   ├── App.css          # Application styles
│   ├── main.jsx         # React entry point
│   └── index.css        # Global styles
├── index.html            # HTML template
├── package.json          # Dependencies and scripts
├── vite.config.js        # Vite configuration
└── README.md             # This file
```

## Components

### App.jsx
The main application component that handles:
- Customer state management
- API communication
- Form handling
- Search functionality
- Customer display

### Key Features

#### Customer Form
- **Name Input**: Required field for customer name
- **Phone Input**: Optional phone number field
- **Amount Input**: Optional numeric amount field
- **Status Dropdown**: Required status selection (yet to pay, processing, paid)
- **Add Button**: Submit customer data to backend

#### Search Functionality
- **Search Input**: Real-time search across all customer fields
- **Search Button**: Manual search trigger
- **Clear Button**: Reset search and show all customers
- **Enter Key Support**: Search on Enter key press

#### Customer Display
- **Customer List**: Displays all customers with their details
- **Status Badges**: Color-coded status indicators
- **Responsive Layout**: Adapts to different screen sizes

## API Integration

### Backend Communication
- **Base URL**: `http://localhost:8000`
- **Endpoints Used**:
  - `GET /customers/` - Fetch all customers
  - `POST /customers/` - Create new customer
  - `GET /customers/search/?q={query}` - Search customers

### Data Flow
1. **Fetch Customers**: Load existing customers on component mount
2. **Add Customer**: Submit form data to create new customer
3. **Search**: Query backend for filtered results
4. **Real-time Updates**: Refresh data after successful operations

## Styling

### Design Principles
- **Modern UI**: Clean, minimalist design
- **Responsive**: Mobile-first responsive design
- **Accessibility**: High contrast and readable fonts
- **Consistency**: Uniform spacing and typography

### Color Scheme
- **Primary**: Blue gradient (#667eea to #764ba2)
- **Success**: Green (#059669)
- **Warning**: Orange (#d97706)
- **Error**: Red (#dc2626)
- **Neutral**: Grays (#718096, #a0aec0)

### Status Colors
- **Yet to Pay**: Red background with red text
- **Processing**: Orange background with orange text
- **Paid**: Green background with green text

## Configuration

### Vite Configuration
The `vite.config.js` file configures:
- Development server settings
- Build optimizations
- Plugin configurations

### Environment Variables
Create a `.env` file in the frontend directory for:
- API base URL
- Environment-specific settings

## Development Workflow

### Adding New Features
1. **Component Creation**: Create new React components in `src/`
2. **Styling**: Add CSS styles in `App.css` or component-specific files
3. **State Management**: Use React hooks for local state
4. **API Integration**: Add new API calls using Axios
5. **Testing**: Test functionality in the browser

### Code Style
- Use functional components with hooks
- Follow React best practices
- Maintain consistent naming conventions
- Add comments for complex logic

## Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   lsof -ti:3000 | xargs kill -9 2>/dev/null || echo "No process on port 3000"
   ```

2. **Dependencies Issues**
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

3. **Build Errors**
   - Check for syntax errors in JSX
   - Verify all imports are correct
   - Check console for error messages

4. **API Connection Issues**
   - Ensure backend server is running
   - Check CORS configuration
   - Verify API endpoint URLs

### Debugging
- Use browser developer tools
- Check console for errors
- Use React Developer Tools extension
- Monitor network requests

## Performance

### Optimization Tips
- Use React.memo for expensive components
- Implement proper dependency arrays in useEffect
- Lazy load components when possible
- Optimize bundle size with code splitting

### Build Optimization
- Vite automatically optimizes builds
- Tree shaking removes unused code
- Minification reduces file sizes
- Asset optimization for images and fonts

## Browser Support

- **Modern Browsers**: Chrome 90+, Firefox 88+, Safari 14+
- **Mobile**: iOS Safari 14+, Chrome Mobile 90+
- **IE**: Not supported (use modern browsers)

## Contributing

1. Follow the existing code style
2. Test changes in multiple browsers
3. Ensure responsive design works
4. Update documentation as needed

## License

This project is open source and available under the MIT License.
