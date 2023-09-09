import './App.css';
import { Routes, Route, Navigate, BrowserRouter } from "react-router-dom";
import Home from "./components/Home"

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate replace to="/home" />} />
          <Route path="/home" element={<Home />} />
          <Route path="/thread" />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
