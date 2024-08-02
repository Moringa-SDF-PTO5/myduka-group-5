import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home.jsx'
import LoginPage from './features/login/page.jsx'
import Layout from './Components/Layout.jsx'
import ProductsPage from './pages/ProductsPage.jsx'
import Dashboardpage from './features/dashboard/page.jsx'
import SupplyRequest from './pages/SupplyRequest.jsx'
<<<<<<< HEAD
import UsersPage from './features/users/page.jsx'
=======
import ProductItemPage from './pages/ProductItemPage.jsx'
import AddProduct from './pages/AddProduct.jsx'
import Payments from './pages/Payments.jsx'
>>>>>>> c2958b3628ac5607320693885c44eec54f0442b5

function App() {
    return (
        <>
            <BrowserRouter>
                <Routes>
                    <Route
                        path='/'
                        element={<Home />}
                    />
                    <Route
                        path='/login'
                        element={<LoginPage />}
                    />
                    <Route element={<Layout />}>
                        <Route
                            path='/dashboard'
                            element={<Dashboardpage />}
                        />
                        <Route
                            path='/products'
                            element={<ProductsPage />}
                        />
                        <Route
                            path='/supply_requests'
                            element={<SupplyRequest />}
                        />
                        <Route
<<<<<<< HEAD
                            path='/users'
                            element={<UsersPage />}
                        />
                    
=======
                            path='/products/:productItemId'
                            element={<ProductItemPage />}
                        />
                        <Route
                            path='/addproduct'
                            element={<AddProduct />}
                        />
                        <Route
                            path='/payments'
                            element={<Payments />}
                        />
>>>>>>> c2958b3628ac5607320693885c44eec54f0442b5
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App
