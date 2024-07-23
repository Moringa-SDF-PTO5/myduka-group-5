import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { store } from "./store/store.js";
import App from "./App.jsx";
import LoginPage from "./features/login/page.jsx";
import Layout from "./Components/Layout.jsx";
import "./index.css";
import ProductsPage from "./features/products/page.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route element={<Layout />}>
            <Route path="/dashboard" element={<App />} />
            <Route path="/products" element={<ProductsPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </Provider>
  </React.StrictMode>
);
