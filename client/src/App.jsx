import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home.jsx'
import LoginPage from './features/login/page.jsx'
import Layout from './Components/Layout.jsx'
import ProductsPage from './pages/ProductsPage.jsx'
import Dashboardpage from './features/dashboard/page.jsx'
import SupplyRequest from './pages/SupplyRequest.jsx'

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
                    </Route>
                </Routes>
            </BrowserRouter>
        </>
    )
}

export default App
