import logo from './logo.svg';
import './App.css';
import FormGroup from '@mui/material/FormGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Pdf from './Sprint5.pdf';

function App() {
  return (
    <div className="App">
<header className="App-header">
  <img src={logo} className="App-logo" alt="logo" />
  <h3>
    Technologies Installed
  </h3>

  <p>
    NGINX
  </p>
  <p>
    REACT
  </p>
  <p>
   CSS Styling: Material UI
  </p>
  <p>
    JQuery
  </p>
  <a
    className="App-link"
    // href="https://reactjs.org"
    href = {Pdf} 
    target = "_blank"
    // rel="noopener noreferrer"
  >
    Sprint 5 Details
  </a>
</header>
</div>
  );
}

export default App;
