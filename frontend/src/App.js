import { BrowserRouter, Routes, Route } from "react-router-dom";
import Products from "./pages/Products";
import Bookings from "./Pages/Bookings";
import Dashboard from "./Pages/Dashboard";
import UserProfile from "./Pages/UserProfile";
import Login from "./Pages/login";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="login" element={<Login />} />
        <Route path="products" element={<Products />} />
        <Route path="bookings" element={<Bookings />} />
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="user" element={<UserProfile />} />
      </Routes>
    </BrowserRouter>
  );
}
