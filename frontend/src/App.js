import './App.css';
import { Routes, Route, Navigate, BrowserRouter } from "react-router-dom";
import Home from "./components/Home"
import Thread from "./components/Thread"

function App() {
  return (
    <div className="App">
      <Thread></Thread>
    </div>
  );
}

export default App;
