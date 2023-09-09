import './App.css';
import "./components/Home";
import { Routes, Route, Navigate, BrowserRouter } from "react-router-dom";
import Home from "./components/Home"
import Thread from "./components/Thread"

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Navigate replace to="/home" />} />
          <Route path="/home" element={<Thread />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
