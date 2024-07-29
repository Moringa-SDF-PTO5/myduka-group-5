import React from "react";
import ReactDOM from "react-dom/client";
import { Provider } from "react-redux";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { store } from "./store/store.js";
// import App from "./App.jsx";
import LoginPage from "./features/login/page.jsx";
import Layout from "./Components/Layout.jsx";
import "./index.css";
import ProductsPage from "./features/products/page.jsx";
import Dashboardpage from "./features/dashboard/page.jsx";
import UsersPage from "./features/users/page.jsx";
import {
    QueryClient,
    QueryClientProvider,
  } from '@tanstack/react-query'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import RecordsPage from "./features/records/page.jsx";
import StoresPage from "./features/stores/page.jsx";

const queryClient = new QueryClient()


ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
    <Provider store={store}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route element={<Layout />}>
            <Route path="/dashboard" element={<Dashboardpage />} />
            <Route path="/products" element={<ProductsPage />} />
            <Route path="/users" element={<UsersPage />} />
            <Route path="/records" element={<RecordsPage />} />
            <Route path="/stores" element={<StoresPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </Provider>
    <ReactQueryDevtools initialIsOpen={false} />
    </QueryClientProvider>
  </React.StrictMode>
);
