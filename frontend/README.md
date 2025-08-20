# Logbook Frontend

A modern React-based frontend application for the Logbook customer management system, now with full Docker support and enhanced development workflow.

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# From project root - starts frontend, backend, and database
./start-docker.sh

# Access frontend at: http://localhost:3000
```

### Option 2: Local Development
```bash
cd frontend
npm install
npm run dev

# Access at: http://localhost:3000
```

## ✨ Features

- **Customer Management**: Add, view, and manage customer records
- **Payment Status Tracking**: Visual status indicators for payment tracking
- **Search Functionality**: Search customers across all fields in real-time
- **Responsive Design**: Modern, mobile-friendly user interface
- **Real-time Updates**: Instant feedback and data synchronization
- **Form Validation**: Client-side validation for better user experience
- **Docker Support**: Full containerization with hot-reload
- **Auto-reload**: Code changes automatically refresh the browser

## 🐳 Docker Support

### Development Container
```bash
# Start all services
docker compose up --build

# View frontend logs
docker compose logs -f frontend

# Restart frontend after changes
docker compose restart frontend
```

### Container Features
- **Hot Reload**: Code changes automatically refresh the browser
- **Volume Mounting**: Local code changes are immediately reflected
- **Network Isolation**: Secure communication with backend
- **Consistent Environment**: Same setup across all machines

## 🛠️ Tech Stack

- **Framework**: React 18+ with modern hooks
- **Build Tool**: Vite for fast development and building
- **Styling**: Custom CSS with modern design principles
- **HTTP Client**: Axios for API communication
- **State Management**: React useState and useEffect hooks
- **Containerization**: Docker with Node.js 18 Alpine image

## 📱 User Interface

### Customer Form
- **Name Input**: Required field for customer name
- **Phone Input**: Optional phone number field
- **Amount Input**: Optional numeric amount field
- **Status Dropdown**: Required status selection (yet to pay, processing, paid)
- **Add Button**: Submit customer data to backend

### Search Functionality
- **Search Input**: Real-time search across all customer fields
- **Search Button**: Manual search trigger
- **Clear Button**: Reset search and show all customers
- **Enter Key Support**: Search on Enter key press

### Customer Display
- **Customer List**: Displays all customers with their details
- **Status Badges**: Color-coded status indicators
- **Responsive Layout**: Adapts to different screen sizes

## 🔌 API Integration

### Backend Communication
- **Base URL**: `http://localhost:8000` (or backend container URL)
- **Endpoints Used**:
  - `GET /customers/` - Fetch all customers
  - `POST /customers/` - Create new customer
  - `GET /customers/search/?q={query}` - Search customers

### Data Flow
1. **Fetch Customers**: Load existing customers on component mount
2. **Add Customer**: Submit form data to create new customer
3. **Search**: Query backend for filtered results
4. **Real-time Updates**: Refresh data after successful operations

## 🎨 Styling

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

## 🔧 Development Workflow

### With Docker (Recommended)
1. **Edit code** in your local directory
2. **Changes auto-reload** in the browser
3. **View logs** for any errors:
   ```bash
   docker compose logs -f frontend
   ```

### Local Development
1. **Install dependencies**: `npm install`
2. **Start dev server**: `npm run dev`
3. **Make changes** and see them in real-time
4. **Build for production**: `npm run build`

### Adding New Features
1. **Component Creation**: Create new React components in `src/`
2. **Styling**: Add CSS styles in `App.css` or component-specific files
3. **State Management**: Use React hooks for local state
4. **API Integration**: Add new API calls using Axios
5. **Testing**: Test functionality in the browser

## 🚨 Troubleshooting

### Docker Issues
1. **Container not starting**
   ```bash
   # Check Docker status
   docker info
   
   # View logs
   docker compose logs frontend
   ```

2. **Code changes not reflecting**
   ```bash
   # Restart frontend container
   docker compose restart frontend
   ```

3. **Port conflicts**
   ```bash
   # Stop all containers
   docker compose down
   
   # Restart
   ./start-docker.sh
   ```

### Local Development Issues
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

### API Connection Issues
- Ensure backend server is running
- Check CORS configuration
- Verify API endpoint URLs
- Check network connectivity between containers

## 📊 Performance

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

## 🌐 Browser Support

- **Modern Browsers**: Chrome 90+, Firefox 88+, Safari 14+
- **Mobile**: iOS Safari 14+, Chrome Mobile 90+
- **IE**: Not supported (use modern browsers)

## 📝 Recent Updates

- ✅ **Docker Integration**: Full containerization with hot-reload
- ✅ **Auto-reload**: Code changes automatically refresh the browser
- ✅ **Container Networking**: Secure communication with backend
- ✅ **Volume Mounting**: Local development with container benefits
- ✅ **Enhanced Workflow**: Streamlined development process

## 📄 License

This project is open source and available under the MIT License.
