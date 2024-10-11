import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Main from './components/Main/Main';
import UserTable from './components/UserTable/UserTable';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/users" element={<UserTable />} />
      </Routes>
    </Router>
  );
}

export default App;