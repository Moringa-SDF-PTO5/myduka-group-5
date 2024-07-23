import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import {BrowserRouter,Routes, Route} from 'react-router-dom'
import { store } from './store/store.js'
import App from './App.jsx'
import LoginPage from './features/login/page.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Provider store={store}>
            <BrowserRouter>
                <Routes>
                    <Route path='/login' element={<LoginPage />} />
                    <Route path='/dashboard' element={<App />} />
                </Routes>
            </BrowserRouter>
        </Provider>
    </React.StrictMode>
)
