import React from 'react'
import {Outlet} from 'react-router-dom'
import {useSelector} from 'react-redux'
import Sidebar from './Sidebar.jsx'
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';


export default function Layout(){
    const state = useSelector(state => state.user);

    return <div className='flex'>
        <Sidebar role={state.user.role}/>
        <main className='grow ml-16 md:ml-64 h-full lg:h-screen bg-gray-100 text-gray-900'>
            <header className='bg-gray-100 text-gray-900 border-b border-gray-300 p-4 flex justify-between items-center'>
                <button className='text-2x1 text-dark'>
                    <Brightness4Icon />
                    <Brightness7Icon />
                </button>
            </header>
            <main className='flex-1 px-8 py-4'>
                <Outlet />
            </main>
        </main>
    </div>
}